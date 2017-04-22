    // Copyright: 2015 AlignAlytics
    // License: "https://github.com/PMSI-AlignAlytics/dimple/blob/master/MIT-LICENSE.txt"
    // Source: /src/methods/_arrayIndexCompare.js
    dimple._arrayIndexCompare = function (array, a, b) {
        // Find the element which comes first in the array
        var returnValue,
            p,
            q,
            aMatch,
            bMatch,
            rowArray;
        for (p = 0; p < array.length; p += 1) {
            aMatch = true;
            bMatch = true;
            rowArray = [].concat(array[p]);
            for (q = 0; q < a.length; q += 1) {
                aMatch = aMatch && (a[q] === rowArray[q]);
            }
            for (q = 0; q < b.length; q += 1) {
                bMatch = bMatch && (b[q] === rowArray[q]);
            }
            if (aMatch || bMatch) {
                if (aMatch && bMatch) {
                    returnValue = 0;
                } else if (aMatch) {
                    returnValue = -1;
                } else {
                    returnValue = 1;
                }
                break;
            }
        }
        return returnValue;
    };
