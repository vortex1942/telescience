import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import { FormControl, Select, Paper } from '@material-ui/core';

const styles = theme => ({
    paper: {
        position: 'relative',
        marginTop: theme.spacing.unit,
        marginRight: theme.spacing.unit,
    },
    textField: {
        margin: theme.spacing.unit,
        width: `calc(100% - ${theme.spacing.unit * 2}px)`,
    },
});

const MapSelect = props => {
    const { classes, selectMap, selectedMap } = props;

    return (
        <Paper className={classes.paper}>
            <FormControl className={classes.textField}>
                <Select
                    MenuProps={classes.menu}
                    native
                    value={selectedMap}
                    onChange={e => {
                        let val = e.target.value;
                        
                        return selectMap(val);
                    }}
                >
                    <option value="faintSignal">Debris Field</option>
                    <option value="cogmap1">Cogmap 1</option>
                    <option value="cogmap2">Cogmap 2</option>
                    <option value="donut2">Donut 2</option>
                    <option value="donut3">Donut 3</option>
                    <option value="nadir">Nadir</option>
                    <option value="kondaru">Kondaru</option>
                    <option value="oshan">Oshan</option>
                    <option value="clarion">Clarion</option>
                    <option value="atlas">Atlas</option> 
                    <option value="neon">Neon</option>
                    <option value="pod_wars">Pod Wars</option>
                    <option value="wrestlemap">Wrestlemap</option>
                    <option value="ozymandias">Ozymandias</option>  
                    <option value="decarabia">Decarabia</option>        
                </Select>
            </FormControl>
        </Paper>
    );
};

export default withStyles(styles)(MapSelect);
