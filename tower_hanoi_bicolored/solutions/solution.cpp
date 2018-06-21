// evaluation_assert data["goals"]["optimal_num_moves"]
// evaluation_assert data["goals"]["optimal_list_of_moves_without_pegs"]
// evaluation_assert data["goals"]["optimal_list_of_moves_with_pegs"]
// evaluation_assert data["goals"]["correct_list_of_moves_with_pegs"]


#include <cstdio>
#include <cassert>
#include <cmath>



void move_tower(int n, int from, int to, int aux);
int min_num_moves(int n);
void move_disk(int disk, int from, int to);
void bicolorProblem(int from, int to, int aux, int n);
void easyBicolor(int from, int to, int aux, int n);
void swapBaseDiskProblem(int from, int to, int aux, int n);
void splitProblem(int from, int to, int aux, int n);
void mergeProblem(int from, int to, int aux, int n);
void enhancedDoubleTowersOfHanoi(int from, int to, int aux, int n);
void doubleTowersOfHanoi(int from, int to, int aux, int n);

void move_disk(int disk, int from, int to);

int min_num_moves(int n, int from, int to, int aux) {
  int moves = 0;
  assert(n>=0);
  switch(n) {
    case 0:
	moves = 0;
    	break;
    case 1:
	moves = 3;
	break;
    case 2:
	moves = 10;
	break;
    default:
	moves = 11*(pow(2, n-1)-1)-3*(n-2);
	break;
  }

  return moves;

}

void bicolorProblem(int n, int from, int to, int aux) {
	assert(n>=1);
	if(n==1) {
		move_disk(n, from, aux);
		move_disk(n, to, from);
		move_disk(n, aux, to);
	} else {
		easyBicolor(from, to, aux, n-1);
		swapBaseDiskProblem(from, to, aux, n);
	}
}

void easyBicolor(int from, int to, int aux, int n) {
	assert(n>=1);
	if(n==1) {
		fprintf(stderr, "Non faccio niente.\n");
	} else {
		bicolorProblem(n-1, from, to, aux);
	}
}

void swapBaseDiskProblem(int from, int to, int aux, int n) {
	if(n==1) {
		move_disk(n, from, aux);
		move_disk(n, to, from);
		move_disk(n, aux, to);
	} else {
		mergeProblem(from, to, aux, n-1);
		move_disk(n, to, aux);
		doubleTowersOfHanoi(from, aux, to, n-1);
		move_disk(n, from, to);
		doubleTowersOfHanoi(aux, to, from, n-1);
		move_disk(n, aux, from);
		enhancedDoubleTowersOfHanoi(to, from, aux, n-1);
		splitProblem(from, to, aux, n-1);	
	}
}

void splitProblem(int from, int to, int aux, int n) {
	if(n==1) {
		move_disk(n, from, to);
	} else {
		doubleTowersOfHanoi(from, aux, to, n-1);
		move_disk(n, from, to);
		doubleTowersOfHanoi(aux, from, to, n-1);
		splitProblem(from, to, aux, n-1);
	}
}

void mergeProblem(int from, int to, int aux, int n) {
	if(n==1) {
		move_disk(n, to, from);
	} else {
		mergeProblem(from, to, aux, n-1);
		doubleTowersOfHanoi(from, aux, to, n-1);
		move_disk(n, to, from);
		doubleTowersOfHanoi(aux, from, to, n-1);
	}
}

void enhancedDoubleTowersOfHanoi(int from, int to, int aux, int n) {
	doubleTowersOfHanoi(from, aux, to, n);
	doubleTowersOfHanoi(aux, to, from, n);
}

void doubleTowersOfHanoi(int from, int to, int aux, int n) {
	if(n==1) {
		move_disk(n, from, to);
		move_disk(n, from, to);
	} else {
		doubleTowersOfHanoi(from, aux, to, n-1);
		move_disk(n, from, to);
		move_disk(n, from, to);
		doubleTowersOfHanoi(aux, to, from, n-1);
	}
}

