/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const mp = new Map();
    const fin = [];
    for(const elm of strs) {
       const sorted = elm.split('').sort().join('');
        if(mp.has(sorted)){
             fin[mp.get(sorted)].push(elm);
        }else{
            mp.set(sorted, fin.length);
            fin.push([elm]);
        }
    }

    return  fin;
};