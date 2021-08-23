import React, {useState, useContext} from 'react';
import { MDBIcon, MDBListGroup, MDBListGroupItem,MDBBadge
} from "mdbreact";
import _ from "lodash";
import {useTranslation} from "react-i18next";

import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogTitle from '@material-ui/core/DialogTitle';
import { useSnackbar } from 'notistack';
import SyncStatus from '../../utils/SyncStatus';
import CompareTgContext from '../../contexts/CompareTgContext';
import {STRG_KEY_NAME} from "../../consts/localStorage";
import {KEY_NAME} from "../../consts/keyName";
import {MSG} from "../../consts/message";
import {SUCCESS} from "../../consts/alert";
import {ROUTER_URL} from "../../consts/router";

const Compare = () => {
  const { setCompareTg } = useContext(CompareTgContext);
  const { t } = useTranslation();
  const { enqueueSnackbar } = useSnackbar();
  const [open, setOpen] = useState(false);
  const compareTg = SyncStatus.get({storageKey: STRG_KEY_NAME.COMPARE}) || [];

  const removeCompareTgBtn = (shareCode) => {
    SyncStatus.remove({
      storageKey: STRG_KEY_NAME.COMPARE, 
      statusSetter: setCompareTg, 
      data: compareTg,
      rmFunc: v => v[KEY_NAME.SHARE_CODE] == shareCode,
    });

    enqueueSnackbar(MSG.REMOVE_COMPARE_TG, {variant: SUCCESS});
  }

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = (value) => {
    setOpen(false);
  };

  return (
    <div>
      <Button className="w-100 h-100" variant="outlined" color="primary" onClick={handleClickOpen}>
        <span>{t('common.compare.compareTgShares')}</span>
        <MDBBadge color="danger" className="ml-2">{compareTg.length}</MDBBadge>
      </Button>


      <Dialog onClose={handleClose} aria-labelledby="simple-dialog-title" open={open}>
        <DialogTitle id="simple-dialog-title">{t('common.compare.compareTgList')}</DialogTitle>
          <MDBListGroup>
            {compareTg.length > 0?
                compareTg.map((v, i) => {
                  return (
                    <MDBListGroupItem>
                      <a className="mr-1" href={`${ROUTER_URL.SHARE_SEARCH}/${v.shareCode}/${v.shareName}`} target="_blank">
                          <span className="h3">{`${v.shareCode}:${v.shareName}`}</span>
                      </a>
                      <MDBIcon className="float-right red-text" onClick={e => {removeCompareTgBtn(v.shareCode)}} icon="times" />
                    </MDBListGroupItem>
                )})
              :<MDBListGroupItem>{t('common.compare.noneSelectedCompareTg')}</MDBListGroupItem>}
          </MDBListGroup>
      </Dialog>
    </div>
    );
}

export default Compare;