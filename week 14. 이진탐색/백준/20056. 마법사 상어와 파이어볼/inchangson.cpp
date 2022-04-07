#include <stdio.h>
#include <algorithm>

//#define DEBUG

#ifdef DEBUG
#define print printf
#else
#define print
#endif

constexpr int MX_N = 50;
constexpr int MX_M = MX_N * MX_N;
constexpr int MX_S = 1000;

constexpr int DIR_NO = 8;
constexpr int DIRS[DIR_NO][2] = {{-1, 0}, {-1, 1},
								  {0, 1}, {1, 1},
								  {1, 0},{1, -1},
								  {0, -1},{-1, -1}
								};


struct Fireball{
	int _row, _col, _mass, _speed, _dir;
};

Fireball stableBalls[4*MX_M];
Fireball movingBalls[4*MX_M];

int g_n;
int g_m;
int g_k;

int stableCnt;
int movingCnt;

void inputData(){
	int tmp_r, tmp_c, tmp_m, tmp_s, tmp_d;
	scanf("%d %d %d", &g_n, &g_m, &g_k);
	for (int idx = 0; idx < g_m; ++idx){
		scanf("%d %d %d %d %d", &tmp_r, &tmp_c, &tmp_m, &tmp_s, &tmp_d);
		stableBalls[idx] = {tmp_r, tmp_c, tmp_m, tmp_s, tmp_d};
	}
	stableCnt = g_m;
}

void printData(){
	print("%d %d %d\n", g_n, g_m, g_k);
	for (int idx = 0; idx < g_m; ++idx){
		print("r %d c %d m %d s %d d %d\n",
		stableBalls[idx]._row, stableBalls[idx]._col,
		 stableBalls[idx]._mass, stableBalls[idx]._speed, stableBalls[idx]._dir
		);
	}
}

void printStable(){
	print("stable>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n");
	for(int idx = 0; idx < stableCnt; ++idx){

		print("r %d c %d m %d s %d d %d\n",
		stableBalls[idx]._row, stableBalls[idx]._col,
		 stableBalls[idx]._mass, stableBalls[idx]._speed, stableBalls[idx]._dir
		);
	}
	print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n");
}

void printMoving(){
	print("moving>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n");
	for(int idx = 0; idx < movingCnt; ++idx){
		print("r %d c %d m %d s %d d %d\n",
		movingBalls[idx]._row, movingBalls[idx]._col,
		 movingBalls[idx]._mass, movingBalls[idx]._speed, movingBalls[idx]._dir
		);
	}
	print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n");
}

void moveFireball(){
#ifdef DEBUG
	print("moveFireball>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n");
	printStable();
	printMoving();
#endif
	for (int idx = 0; idx < stableCnt; ++idx){
		Fireball ball = stableBalls[idx];
		ball._row = ball._row + ball._speed * DIRS[ball._dir][0];
		ball._col = ball._col + ball._speed * DIRS[ball._dir][1];

		ball._row += MX_S*g_n;
		ball._col += MX_S*g_n;


		ball._row %= g_n;
		ball._col %= g_n;
		
		//append to movingBalls
		movingBalls[movingCnt++] = ball;
	}
	stableCnt = 0;
#ifdef DEBUG
	printStable();
	printMoving();
	print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n");
#endif

}

bool compare(const Fireball& fb1, const Fireball& fb2){
	
	if (fb1._row < fb2._row){
		return false;
	}
	if (fb1._row > fb2._row){
		return true;
	}
	if (fb1._col > fb2._col){
		return true;
	}
	return false;
}

void sortMovingBalls(){
#ifdef DEBUG
	print("sortMovingBalls>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n");
	printMoving();
#endif

	std::sort(movingBalls, movingBalls + movingCnt, compare);

//	for (int i = 0; i < movingCnt; ++i){
//		for (int j = i+1; j < movingCnt; ++j){
//			Fireball b1 = movingBalls[i];
//			Fireball b2 = movingBalls[j];
//			if (b1._row < b2._row){
//				continue;
//			}
//			if (b1._row == b2._row && b1._col <= b2._col){
//				continue;
//			}
//			movingBalls[i] = b2;
//			movingBalls[j] = b1;
//		}
//	}
#ifdef DEBUG
	printMoving();
	print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n");
#endif


}


void mergeFireball(){
#ifdef DEBUG
	print("mergeFireball>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n");
	printStable();
	printMoving();
#endif
	//sort
	sortMovingBalls();
//===========================================

	Fireball pivot, tmp;
	
	int start, end;
	int r, c, m, s, cnt;
	bool isPivotOdd, isRsltDirOdd;
	//combine
	for( start = 0; start < movingCnt; ++start){
		
#ifdef DEBUG
	print("=============================================\n");
	print("=============================================\n");
	printStable();
	printMoving();
#endif

		isRsltDirOdd = false;
		cnt = 1;
		pivot = movingBalls[start];
		r = pivot._row;
		c = pivot._col;
		m = pivot._mass;
		s = pivot._speed;
		isPivotOdd = (pivot._dir) % 2;
		
		end = start + 1;
		while (1){
			if(end >= movingCnt){
				break;
			}

			tmp = movingBalls[end];
			
			if(!(tmp._row == r && tmp._col == c)){
				break;
			}
				
			m += tmp._mass;
			s += tmp._speed;

			if (isPivotOdd != ((tmp._dir) % 2)){
				isRsltDirOdd = true;
			}
			
			cnt++;
			end++;
		}

		if (cnt > 1){
			m /= 5;
			s /= cnt;
			
			if(m){
				stableBalls[stableCnt++] = {r, c, m, s, 0 + (int)isRsltDirOdd};
				stableBalls[stableCnt++] = {r, c, m, s, 2 + (int)isRsltDirOdd};
				stableBalls[stableCnt++] = {r, c, m, s, 4 + (int)isRsltDirOdd};
				stableBalls[stableCnt++] = {r, c, m, s, 6 + (int)isRsltDirOdd};
			}
		}

		else{
			stableBalls[stableCnt++] = pivot;
		}
		
		start = end - 1;
#ifdef DEBUG
	printStable();
	printMoving();
	print("=============================================\n");
	print("=============================================\n");
#endif

	}
	movingCnt = 0;
	
#ifdef DEBUG
	printStable();
	printMoving();
	print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n");
#endif
}

int getTotalMass(){
	int sum = 0;
	for(int i = 0; i < stableCnt; ++i){
		sum += stableBalls[i]._mass;
	}
	return sum;
}

int solve(void){
	while (g_k--){
		// move fireballs
		// ball_arr1 -> ball_arr2
		moveFireball();

		// update fireballs(combine, split)
		// ball_arr2 -> ball_arr1
		mergeFireball();
	}
	
	return getTotalMass();
}

void testSort(){

#ifdef DEBUG
	printStable();
	printMoving();
#endif

	moveFireball();
	sortMovingBalls();
	
#ifdef DEBUG
	printStable();
	printMoving();
#endif
}

int main(void){
	inputData();
	//printData();

	//testSort();

	printf("%d\n", solve());
	return 0;
}
