import React from 'react';

const Images = ({ selectedMap, image }) => {
    const info = mapInfo(selectedMap);
    return (
        <div onDragStart={e => e.preventDefault()}>
            {(() => {
                const arr = [];
                for (let i = 0; i < 8; i++) {
                    for (let g = 0; g < 8; g++) {
                        arr.push(`${i},${g}`);
                    }
                }
                return arr;
            })().map(url => {
                return <img className={image} key={url} alt={url} src={`${info}/${url}.png`} />;
            })}
        </div>
    );
    function mapInfo(selectedMap) {
        const info = {
            cogmap1: `/images/cogmap1/`,
            cogmap2: `/images/cogmap2/`,
            faintSignal: `/images/faintSignal/`,
            oshan: `/images/oshan/`,
            clarion: `/images/clarion/`,
            destiny: `/images/destiny/`,
            atlas: `/images/atlas/`,
            //horizon: `/images/horizon/`,
            //mushroom: `/images/mushroom/`,
            //manta: `/images/manta/`,
            kondaru: `/images/kondaru/`,
            donut2: `/images/donut2/`,
            //fleet: `/images/fleet/`,
            donut3: `/images/donut3/`,
        };   
        if (!info[selectedMap]) return info['cogmap1'];
        return info[selectedMap];
    }
};

export default Images;
