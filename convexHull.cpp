#include <bits/stdc++.h>

using namespace std;

struct xy{
    double x, y;
    xy() : x(0.0), y(0.0) {}
    xy(double _x, double _y) : x(_x), y(_y) {}
};

ostream& operator<<(ostream& os, const vector<xy>& points){
    for(int x{}; x < points.size(); ++x){
        os << "(" << points[x].x << ", " << points[x].y << ")" << "\n";
    }
    return os;
}

double determinant(const xy& u, const xy& v, const xy& p){
    /*
        | x2-x1  x-x1 |
        | y2-y1  y-y1 | = ad - bc
    */
   double ad = (v.x-u.x)*(p.y-u.y);
   double bc = (p.x-u.x)*(v.y-u.y);
   return (ad - bc);
}

vector<xy> convexHullBruteForce(const vector<xy>& points){
    vector<xy> convex_hull;
    /* consider every pair of points */
    for(int u{}; u < points.size(); ++u){
        for(int v{}; v < points.size(); ++v){
            if(u == v) continue;
            // check if all other points are on the same side (or colinear) of the line segment u, v
            bool all_same_side = true; // assume all points are on same side (same determinant sign)
            for(int p{}; p < points.size() - 1; ++p){
                double d1 = determinant(points[u], points[v], points[p]);
                double d2 = determinant(points[u], points[v], points[p+1]);
                bool s1   = (d1 <= 0 ? 0 : 1);
                bool s2   = (d2 <= 0 ? 0 : 1);
                if(s1 ^ s2){ all_same_side = false; break; }
            }
            if(all_same_side){ // if all points were actually on the same side, add v (maybe u) to convex hull
                 convex_hull.push_back(points[v]);
            }
        }
    }
    return convex_hull;
}

int main(){
    vector<xy> points = {
        xy{-8,-2}, xy{-3,-7}, xy{-3,-4}, xy{0,-1}, xy{5,-9},
        xy{5,-3},  xy{6,-6},  xy{7,-5},  xy{8,-8}, xy{9,0}
    };

    vector<xy> ch = convexHullBruteForce(points);
    cout << "Convex Hull: \n";
    for(auto it = ch.begin(); it != ch.end(); ++it)
        cout << "(" << it->x << ", " << it->y << ")" << endl;
    
    return 0;
}