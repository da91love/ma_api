/* eslint-disable no-use-before-define */
import React from 'react';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import {KEY_NAME, OTHER_KEY_NAME} from '../../consts/keyName';
import {ROUTER_URL} from '../../consts/router';
import { useHistory } from 'react-router-dom';

const SearchInput = (props) => {
    // Top 100 films as rated by IMDb users. http://www.imdb.com/chart/top
    const {options} = props;
    const history = useHistory();

    const searchHandler = (e, value) => {
        if (value) {
            history.push({
                pathname: ROUTER_URL.SHARE_SEARCH,
                state: {
                    [KEY_NAME.SHARE_CODE]: value[KEY_NAME.SHARE_CODE],
                    [KEY_NAME.SHARE_NAME]: value[KEY_NAME.SHARE_NAME],
                },
            })
        }
    }

    return (
        <Autocomplete
            id="combo-box-demo"
            options={options}
            getOptionLabel={(option) => option['target']}
            style={{ width: 400 }}
            onChange={searchHandler}
            renderInput={(params) => <TextField {...params} label="Search" variant="outlined"/>}
        />
    );
}

export default SearchInput;

