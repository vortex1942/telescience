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
            cogmap1: `images/cogmap1/`,
            cogmap2: `images/cogmap2/`,
            faintSignal: `images/faintSignal/`,
            nadir: `images/nadir`,
            oshan: `images/oshan/`,
            clarion: `images/clarion/`,
            //destiny: `images/destiny/`,
            atlas: `images/atlas/`,
            //horizon: `/images/horizon/`,
            //mushroom: `/images/mushroom/`,
            //manta: `/images/manta/`,
            kondaru: `images/kondaru/`,
            donut2: `images/donut2/`,
            //fleet: `/images/fleet/`,
            donut3: `images/donut3/`,
            /*
            //Leaving this here, Ideally Goonhub will be added to the CI/CD eventually so we don't need to update maps
            cogmap1: `https://goonhub.com/images/maps/cogmap/z1`,
            cogmap2: `https://goonhub.com/images/maps/cogmap2/z1`,
            faintSignal: `https://goonhub.com/images/maps/cogmap2/z3`,
            oshan: `https://goonhub.com/images/maps/oshan/z1`,
            clarion: `https://goonhub.com/images/maps/clarion/z1`,
            destiny: `https://goonhub.com/images/maps/destiny/z1`,
            atlas: `https://goonhub.com/images/maps/atlas/z1`,
            horizon: `https://goonhub.com/images/maps/horizon/z1`,
            mushroom: `https://goonhub.com/images/maps/mushroom/z1`,
            manta: `https://goonhub.com/images/maps/manta/z1`,
            kondaru: `https://goonhub.com/images/maps/kondaru/z1`,
            donut2: `https://goonhub.com/images/maps/donut2/z1`,
            fleet: `https://goonhub.com/images/maps/bellerophon%20fleet/z1`,
            donut3: `https://goonhub.com/images/maps/donut3/z1`,
            */
        };   
        if (!info[selectedMap]) return info['cogmap1'];
        return info[selectedMap];
    }
};

export default Images;
