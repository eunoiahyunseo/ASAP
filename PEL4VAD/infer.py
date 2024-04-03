
import time
from utils import fixed_smooth, slide_smooth
from test import *
import numpy as np



def infer_func(model, dataloader, gt, logger, cfg):
    st = time.time()
    rep = 16
    with torch.no_grad():
        model.eval()
        pred = torch.zeros(0).cuda()
        normal_preds = torch.zeros(0).cuda()
        normal_labels = torch.zeros(0).cuda()
        # gt = np.zeros(5312)
        gt_tmp = torch.tensor(gt.copy()).cuda()

        # v_input: [1, 10*83, 1024]

        for i, (v_input, name) in enumerate(dataloader):
            v_input = v_input.float().cuda(non_blocking=True)
            print(f'v_input: {v_input}, v_input.shape: {v_input.shape}')
            seq_len = torch.sum(torch.max(torch.abs(v_input), dim=2)[0] > 0, 1) # 830
            logits, _ = model(v_input, seq_len)
            logits = torch.mean(logits, 0)
            logits = logits.squeeze(dim=-1)

            seq = len(logits)
            if cfg.smooth == 'fixed':
                logits = fixed_smooth(logits, cfg.kappa)
            elif cfg.smooth == 'slide':
                logits = slide_smooth(logits, cfg.kappa)
            else:
                pass
            logits = logits[:seq]

            pred = torch.cat((pred, logits))
            labels = gt_tmp[: seq_len[0]*rep] # i3d는 64rgb마다니까 *64해준다.
            if torch.sum(labels) == 0:
                normal_labels = torch.cat((normal_labels, labels))
                normal_preds = torch.cat((normal_preds, logits))
            gt_tmp = gt_tmp[seq_len[0]*rep:]

        pred = list(pred.cpu().detach().numpy())
        # print('pred: ', pred)
        # print('gt: ', list(gt))
        # print(f'pred: {pred}, pred.shape: {len(pred)}')
        far = cal_false_alarm(normal_labels, normal_preds)
        fpr, tpr, thresholds = roc_curve(list(gt), np.repeat(pred, rep))
        print(f'fpr: {fpr}, tpr: {tpr}, thresholds: {thresholds}')
        # Youden의 J 지수를 계산
        J = tpr - fpr
        
        # 최대 J 지수를 가진 인덱스를 찾음
        ix = np.argmax(J)
        best_thresh = thresholds[ix]
        print(f'Best Threshold={best_thresh}')
        roc_auc = auc(fpr, tpr)
        pre, rec, _ = precision_recall_curve(list(gt), np.repeat(pred, rep))
        pr_auc = auc(rec, pre)
        np.save('./pred', np.concatenate((pred, [best_thresh])) )
        


    time_elapsed = time.time() - st
    logger.info('offline AUC:{:.4f} AP:{:.4f} FAR:{:.4f} | Complete in {:.0f}m {:.0f}s\n'.format(
        roc_auc, pr_auc, far, time_elapsed // 60, time_elapsed % 60))
