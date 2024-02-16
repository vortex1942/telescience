import React from 'react';

const Images = ({ selectedMap, image }) => {
    const info = mapInfo(selectedMap);
    return (
        <div onDragStart={e => e.preventDefault()}>
            {(() => {
                const arr = [];
                for (let i = 0; i < 10; i++) {
                    for (let g = 0; g < 10; g++) {
                        arr.push(`${g},${i}`);
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
            

            nadir: `https://goonhub.com/storage/maps/nadir`,
            cogmap1: `https://goonhub.com/storage/maps/cogmap`,
            cogmap2: `https://goonhub.com/storage/maps/cogmap2`,
            faintSignal: `https://goonhub.com/storage/maps/debris`,
            oshan: `https://goonhub.com/storage/maps/oshan`,
            clarion: `https://goonhub.com/storage/maps/clarion`,
            destiny: `https://goonhub.com/storage/maps/destiny`,
            atlas: `https://goonhub.com/storage/maps/atlas`,
            manta: `https://goonhub.com/storage/maps/manta`,
            kondaru: `https://goonhub.com/storage/maps/kondaru`,
            donut2: `https://goonhub.com/storage/maps/donut2`,
            donut3: `https://goonhub.com/storage/maps/donut3`,
            adventurezone: `images/adventurezone/`,

        };   
        if (!info[selectedMap]) return info['cogmap1'];
        return info[selectedMap];
    }
};

export default Images;
