let gradient = (x1,x2,y1,y2) => {
    let grad = (y2 - y1) / (x2 - x1)
    return grad
}

let maxpt3 = arr => {
    if(arr.length <= 2) return arr.length
    let dict = {}
    let result = 0
    for(let i = 0; i < arr.length; i++){
        dict = {}
        duplicate = 0
        max = 0
        for(let j = i + 1; j < arr.length; j++){
            // if (arr[j][0] - arr[i][0] == 0 && arr[j][1] - arr[i][1] == 0){
            //     duplicate += 1
            // }
            let m = gradient(arr[i][0], arr[j][0], arr[i][1], arr[j][1]) 
            if(dict[m] == undefined){
                dict[m] = 1
            }else{
                dict[m] += 1
            }
            max = Math.max(max, dict[m])
            
        }
        
        result = Math.max(max+duplicate+1, result)
        
    }
    
    return result
}

console.log(maxpt3([[1, 1],[2, 2],[2, 3],[3, 3],[3, 5]]))