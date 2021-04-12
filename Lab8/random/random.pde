import peasy.*;
float x0=0,y0=0,z0=0;
float x1=0,y1=0,z1=0;
float step = 1, ran;
ArrayList<PVector> p0= new ArrayList<PVector>();
ArrayList<PVector> p1= new ArrayList<PVector>();
PeasyCam cam;
void setup(){
  size(800,800,P3D);
  translate(width/2,height/2);
  colorMode(HSB);
  cam = new PeasyCam(this,400);
  frameRate = 10;
}
void draw(){
  background(0);
  stroke(255);
  scale(4);
  strokeWeight(0.25);
  textSize(20);
  line(0,0,0,50,0,0);
  //text("X",50,0,0);
  line(0,0,0,0,50,0);
  //text("Y",0,50,0);
  line(0,0,0,0,0,50);
  //text("Z",0,0,50);
  ran = floor(random(6));
  if(ran == 0) x1+=step;
  else if(ran == 1) x1-=step;
  else if(ran == 2) y1+=step;
  else if(ran == 3) y1-=step;
  else if(ran == 5) z1+=step;
  else z1-=step;
  p0.add(new PVector(x0,y0,z0));
  p1.add(new PVector(x1,y1,z1));
  float hu=0;
  for(int i=0;i<p0.size();i++){
    stroke(hu,255,255);
    hu += 1;
    hu %= 255;
    //line(p0.get(i).x,p0.get(i).y,p0.get(i).z,p1.get(i).x,p1.get(i).y,p1.get(i).z);
    line(p0.get(i).x,p0.get(i).y,p1.get(i).x,p1.get(i).y);
    //rotateZ(5);
  }
  x0 = x1;
  y0 = y1;
  z0 = z1;
}
