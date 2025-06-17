// Define meshing parameter
h = 0.00008;
lx = 0.04;  // Width of the box (4cm)
ly = 0.018;  // Height of the box (1.8cm)
dx = 0.0049; // rhombus, +-0.0049 half-width (0.98cm)
dy = 0.001225; // rhombus, +-0.001225  half-hight (0.245cm)

// Reactor Wall Points (Box Geometry)
Point(1) = {0, 0, 0, h};
Point(2) = {lx, 0, 0, h};
Point(3) = {lx, ly, 0, h};
Point(4) = {0, ly, 0, h};


// Electrode 1 (right center electrode)
Point(5) =  {0.0051,  0.00885,  0, h};
Point(6) =  {0.0149 - dx,  0.00885 - dy,  0, h}; // (1, 0.007625)
Point(7) =  {0.0149,  0.00915, 0, h};
Point(8) =  {0.0051 + dx,  0.00915 + dy, 0, h}; // (1, 0.010375)

// Electrode 2 (left center electrode)
Point(9)  = {0.0251,  0.00885,  0, h};
Point(10) = {0.0349 - dx,  0.00885 - dy,  0, h}; // (3, 0.007625)
Point(11) = {0.0349,  0.00915, 0, h};
Point(12) = {0.0251 + dx,  0.00915 + dy, 0, h}; // (3, 0.010375)


//Reactor Wall
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Curve Loop(1) = {1, 2, 3, 4};
// Electrode 1 (right center electrode)
Line(5) = {5, 6};
Line(6) = {6, 7};
Line(7) = {7, 8};
Line(8) = {8, 5};
Curve Loop(2) = {5, 6, 7, 8};
// Electrode 2 (left center electrode)
Line(9) = {9, 10};
Line(10) = {10, 11};
Line(11) = {11, 12};
Line(12) = {12, 9};
Curve Loop(3) = {9, 10, 11, 12};

Plane Surface(1) = {1,2,3};

//from 2d in 3d
Extrude {0, 0, 0.001} {Surface{1}; Layers {1}; Recombine;}

//+
Physical Volume("Air", 75) = {1};
//+
Physical Surface("Electrode", 76) = {49, 57, 45, 53, 61, 65, 69, 73};
//+
Physical Surface("In", 77) = {41};
//+
Physical Surface("Top", 78) = {37};
//+
Physical Surface("Out", 79) = {33};
//+
Physical Surface("Bottom", 80) = {29};







// force coordinates-------------------------------------------------------

//central top left has the following coordinates:
//Point(11) = (0.0349,  0.00915, 0)
//Point(12) = (0.03, 0.010375, 0)

//central bottom left has the following coordinates:
//Point(9)  = (0.0251,  0.00885,  0)
//Point(10) = (0.03, 0.007625, 0)

//central top right has the following coordinates:
//Point(7) =  (0.0149,  0.00915, 0)
//Point(8) =  (0.01, 0.010375, 0)

//central bottom right has the following coordinates:
//Point(5) =  (0.0051,  0.00885,  0)
//Point(6) =  (0.01, 0.007625, 0)



