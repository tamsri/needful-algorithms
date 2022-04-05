const assert = require('assert').strict;

function gcd_brute(a, b){
	assert(b > 0);
	assert(a > 0);
	const getMulCommonFactor = (num)=>{
		assert(num>0);
		let current = num;
		let mul_list = [];
		let divider = 2;
		while(current!=1){
			if(current%divider == 0){
				current = current/divider;
				mul_list.push(current);
			}else{
				divider += 1;
			}
		}
		return mul_list;
	}
	let a_list = getMulCommonFactor(a);
	let b_list = getMulCommonFactor(b);
	const getIntersect = (list_one, list_two)=>{
		list_one = list_one.sort();
		list_two = list_two.sort();
		let one_i = 0;
		let two_i = 0;
		let intersect_list = [];
		while(one_i < list_one.length && two_i < list_two.length){
			current_one = list_one[one_i];
			current_two = list_two[two_i];
			if(current_one === current_two){
				intersect_list.push(current_one);
				one_i++;
				two_i++;
			} else if (current_one < current_two){
				one_i++;
			} else {
				two_i++;
			}
		}
		return intersect_list;
	}
	shared_list = getIntersect(a_list, b_list);
	let answer = 1;
	for(const num of shared_list){
		answer *= num;
	}
	return answer;
}

function gcd_euclid(a, b){
	assert(a>0);
	assert(b>0);
	let min_num = Math.min(a,b);
	let max_num = Math.max(a,b);
	while (max_num %min_num != 0){
		const reminder = max_num%min_num;
		max_num = min_num;
		min_num = reminder
	}
	return min_num
}
let answer_1 = gcd_brute(25, 10);
let answer_2 = gcd_euclid(25, 10);
console.log(answer_1);
console.log(answer_2);
