import React from 'react';
import { Button, Popover, Typography } from '@material-ui/core';

const HelperText = () => {
    return (
        <>
            <h3>Help, I'm stuck!</h3>
            <hr />
            <h3>Finding inital values (Ingame)</h3>
            <ol type="1">
                <li>Set the teleporter to X: 100 Y: 50 Z: 0</li>
                <li>Press the Scan button</li>
                <li>If your X or Y coords are invalid Increment them by +25 until valid
                <br></br>&emsp;On the top left of the website change the console coord to any valid ingame coord
                </li>

                <li>If your Z coord is invalid Increment it by +1
                <br></br>&emsp;The 1<sup>st</sup> valid Z level is the Station
                <br></br>&emsp;The 2<sup>nd</sup> valid Z level is the Adventure Zone
                <br></br>&emsp;The 3<sup>rd</sup> valid Z level is the Debris Field / Trench
                </li>
            </ol>

            <h3>Calibrating the website</h3>
            <ol type="1">
                <li>Find a GPS, Change the identifer to "TELE" and toggle distress signal</li>
                <li>Send the GPS to the X2 & Y2 Coordinates</li>
                <li>Using another GPS find the TELE GPS and input it's coordinates in the GPS Column for X1 & Y2</li>
                <li>Repeat the previous two steps for X2 & Y2</li>
                <br></br>
                <li>Click on a visible tile near you, Enter the values from the Console Coordinates box Ingame, and press the receive button
                    <br></br>&emsp;If you see a portal appear on that spot your calibration is accurate
                    <br></br>&emsp;If you do not see a portal, Check coordinates, or repeat GPS calibration
                </li>

                <li>Record the values in the table onto a piece of paper for your fellow scientists</li>
            </ol>
            <p>When you're done, you can close the math table by clicking the "DO TELESCIENCE MATH" header.</p>
            <p>Change maps with the Top Right dropdown box</p>
            <p>Right click anywhere to add favorites.</p>
            <p>ALT + WASD, Arrow Keys, or Numpad to navigate via keyboard.</p>
            <p>
                Stuck? Check the SS13 wiki on{`\t`}
                <Button
                    color="secondary"
                    variant="outlined"
                    size="small"
                    href="https://wiki.ss13.co/Telescience#Decoding_the_teleporter"
                    rel="noopener noreferrer"
                    target="_blank"
                >
                    decoding the teleporter
                </Button>
            </p>
            <p>
                Need more info?{`\t`}
                <Button
                    color="secondary"
                    variant="outlined"
                    size="small"
                    href="https://github.com/vortex1942/telescience"
                    rel="noopener noreferrer"
                    target="_blank"
                >
                    Click here
                </Button>
                {`\t`}for a detailed readme.
            </p>
            <hr />
            <p>Original credit goes to Kayle7777.{`\t`}
            <Button
                color="secondary"
                variant="outlined"
                size="small"
                href="https://github.com/Kayle7777/telescience"
                rel="noopener noreferrer"
                target="_blank"
            >
                Click Here
            </Button>
            {`\t`}for a Kayle7777's github
            </p>
        </>
    );
};

const HelperPopover = props => {
    const { classes, open, anchorEl, onClose, anchorOrigin } = props;
    return (
        <Popover
            className={classes.popOver}
            aria-label="Math help"
            id="math-tips"
            open={open}
            anchorEl={anchorEl}
            onClose={onClose}
            anchorOrigin={anchorOrigin}
        >
            <Typography variant="caption" className={classes.popOverText}>
                <HelperText />
            </Typography>
        </Popover>
    );
};

export default HelperPopover;
