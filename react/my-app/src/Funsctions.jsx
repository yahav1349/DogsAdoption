
function LinearColor({ progress }) {
    return (
        <div style={{ width: '40%', marginTop: '20px' , marginLeft: '200px'}}>
            <LinearProgress
                variant="determinate"
                marginTop="30px"
                marginLeft="30px"
                value={progress}
                color="primary"
            />
            <Typography
                variant="h5"
                component="div"
                style={{ textAlign: 'center', marginTop: '5px' }}
            >
                {`${Math.round(progress)}%`}
            </Typography>
        </div>
    );
}

function CharacterSelect() {
    return (
        <Autocomplete
        id="country-select-demo"
        sx={{ width: 300,  marginBottom: '150px', marginLeft: '200px'}}
        options={characterisitcs}
        autoHighlight
        getOptionLabel={(option) => option.label}
        renderInput={(params) => (
            <TextField
            {...params}
            label="Choose a characterisitc"
            inputProps={{
                ...params.inputProps,
                autoComplete: 'new-password', // disable autocomplete and autofill
            }}
            />
        )}
        />
    );
    }