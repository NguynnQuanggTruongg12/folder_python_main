#define pul1 2
#define dir1 4
#define ena1 6

#define pul2 10
#define dir2 12
#define ena2 14

#define pul3 24
#define dir3 26
#define ena3 28


#define dt1 0.005
#define dt2 0.05
#define dt3 0.05

#define GRIPPER 38

bool flag = false;
bool flag_qh1 = false;
bool flag_qh2 = false;
bool flag_qh3 = false;

volatile long int t=0;

long int vitri=0, vitrimm=0, error=0;

int state1 = 1, state2 = 1, Count1 = 0, PID_COUNT =0, Count2 = 0, state3 =  1, Count3 =0 ;
bool run1 = false;
bool run2 = false;
bool run3 = false;

bool gripper =0;



float xd1_0 = 0, xd1_c = 0, xd1_n = 0, tf1_c = 1,v1_max = 0;
float tf1_n = 1, x1 = 0, t1= 0, step_d =(0.075*11)/(57);  //((1.8/32)/?/)*289/3969
float xd2_0 = 0, xd2_c = 0, xd2_n = 0, tf2_c = 1,v2_max = 0;
float tf2_n = 1, x2 = 0, t2= 0, step_d2 = (0.0421875*289)/(3969); // (1.8/16)/3
float xd3_0 = 0, xd3_c = 0, xd3_n = 0, tf3_c = 1,v3_max = 0;
float tf3_n = 1, x3 = 0, t3= 0, step_d3 = (0.0421875*11)/(57);                           
float a10 = 0, a11 = 0, a12 = 0, a13 = 0, a20 = 0, a21 = 0, a22 = 0, a23 = 0, a30 = 0, a31 = 0, a32 = 0, a33 = 0;
byte savePrescale;



ISR(TIMER1_COMPA_vect)        
{
  step_1();
  step_2();
  step_3();
}

void step_1() {
    float y = 0;
    if (run1 == false && flag_qh1 == false) {
        xd1_c = xd1_n; 
        tf1_c = tf1_n; 
        xd1_0 = x1;

        a10 = xd1_0;
        a11 = 0;
        a12 = 3 * (xd1_c - xd1_0) / (tf1_c * tf1_c);
        a13 = -2 * (xd1_c - xd1_0) / (tf1_c * tf1_c * tf1_c);
        t1 = 0; 
        Count1 = 0; 
        run1 = true; 
        flag_qh1 = true;

        // Thiết lập hướng quay động cơ
        digitalWrite(dir1, (xd1_c > xd1_0) ? HIGH : LOW);
    } else {
        if (abs(x1 - xd1_c) >= (0.5 * step_d)) {
            t1 += dt1;
            y = a10 + a11 * t1 + a12 * t1 * t1 + a13 * t1 * t1 * t1;

            if (abs(y - x1) >= (0.5 * step_d)) {
                if (state1 == 0) {
                    Count1++;
                }
                state1 = 1 - state1;
                digitalWrite(pul1, state1);
                x1 += 0.5 * step_d * ((xd1_c > xd1_0) ? 1 : -1);
            }
        } else {
            run1 = false;
        }
    }
}
void step_2(){
  float y = 0;
  
  if(run2 == false && flag_qh2 == false) 
  {
    xd2_c = xd2_n;
    tf2_c = tf2_n;
    xd2_0 = x2;

    a20 = xd2_0;
    a21 = 0;
    a22 = 3*(xd2_c - xd2_0)/(tf2_c*tf2_c);
    a23 = -2*(xd2_c - xd2_0)/(tf2_c*tf2_c*tf2_c);
    t2 = 0;
    Count2 = 0;
    run2 = true;
    flag_qh2 = true;
  }else
  {
    if(abs(x2 - xd2_c) >= (0.5*step_d2))
   {
    t2 = t2 + dt2;
    y = a20 + a21*t2 + a22*t2*t2 + a23*t2*t2*t2;
    
    if(abs(y - x2) >= (0.5*step_d2))  
    {
      if(state2 == 0)
        Count2 ++;
        state2 = 1 - state2;
        digitalWrite(dir2,((xd2_c>xd2_0)?1:0));
        digitalWrite(pul2,state2);
        x2 += 0.5*step_d2*((xd2_c>xd2_0)?1:-1);
    }
    }else run2 = false;
  }
}
void step_3(){
  float y = 0;
  
  if(run3 == false && flag_qh3 == false) 
  {
    xd3_c = xd3_n;
    tf3_c = tf3_n;
    xd3_0 = x3;

    a30 = xd3_0;
    a31 = 0;
    a32 = 3*(xd3_c - xd3_0)/(tf3_c*tf3_c);
    a33 = -2*(xd3_c - xd3_0)/(tf3_c*tf3_c*tf3_c);
    t3 = 0;
    Count3 = 0;
    run3 = true;
    flag_qh3 = true;
  }else
  {
    if(abs(x3 - xd3_c) >= (0.5*step_d3))
   {
    t3 = t3 + dt3;
    y = a30 + a31*t3 + a32*t3*t3 + a33*t3*t3*t3;
    
    if(abs(y - x3) >= (0.5*step_d3))  
    {
      if(state3 == 0)
        Count3 ++;
        state3 = 1 - state3;
        digitalWrite(dir3,((xd3_c>xd3_0)?1:0));
        digitalWrite(pul3,state3);
        x3 += 0.5*step_d3*((xd3_c>xd3_0)?1:-1);
    }
    }else run3 = false;
  }
}
void setup() {

  noInterrupts();

  pinMode(GRIPPER, OUTPUT);
  digitalWrite(GRIPPER,1);

  pinMode(pul1, OUTPUT);
  pinMode(dir1, OUTPUT);
  pinMode(ena1, OUTPUT);
  digitalWrite(ena1,LOW);

  pinMode(pul2, OUTPUT);
  pinMode(dir2, OUTPUT);
  pinMode(ena2, OUTPUT);
  digitalWrite(ena2,LOW);

  pinMode(pul3, OUTPUT);
  pinMode(dir3, OUTPUT);
  pinMode(ena3, OUTPUT);
  digitalWrite(ena3,LOW);

    
  setup_timer1();

  Serial.begin(115200);
  Serial.setTimeout(10);
  // Serial1.setTimeout(10);

  while(!Serial){
  ;
  }
  delay(500);
  interrupts();

}
void setup_timer1() {
    TCCR1A = 0;
    TCCR1B = 0;
    TCNT1 = 0;

    TCCR1B |= (1 << WGM12);   
    TCCR1B |= (1 << CS11);    
    OCR1A = 125;                
    TIMSK1 |= (1 << OCIE1A);  
}
void serialEvent() {
    String inString = "";    
    String v1, v2, v3, v4;
    int k[4];
    int j = 0;

    if (Serial.available() > 0 && flag) {  
        inString = Serial.readStringUntil('\n');
        // Serial.println("Dữ liệu nhận được: " + inString);  // Thêm dòng này để chẩn đoán

        int lengthString = inString.length();
        for (int i = 0; i < lengthString; i++) {
            char symbol = inString.charAt(i);
            if (symbol == ';') { // Kiểm tra dấu ';'
                k[j] = i;
                j++;
            }
        }

        // Thêm kiểm tra để đảm bảo đủ số lượng phần tử
        if (j < 3) {
            // Serial.println("Không đủ giá trị để tách.");
            return; // Kết thúc nếu không đủ
        }

        // Tách các giá trị dựa trên dấu ';'
        v1 = inString.substring(0, k[0]);
        v2 = inString.substring(k[0] + 1, k[1]);
        v3 = inString.substring(k[1] + 1, k[2]);
        v4 = inString.substring(k[2] + 1, lengthString);

        // Chuyển đổi các giá trị từ chuỗi sang số
        xd1_n = v1.toFloat(); // Biến thứ nhất
        xd2_n = v2.toFloat(); // Biến thứ ba
        xd3_n = v3.toFloat();
        // xd2_n = xd2_n_1 + 90;
        // xd3_n = xd3_n_1 + 90;
        gripper = v4.toInt();    // Biến thứ tư
        tf1_n = 15; // Biến thứ hai
        tf2_n = 5;
        tf3_n = 5;
        // In ra các giá trị đã nhận
        Serial.print("xd1_n: ");
        Serial.print(xd1_n);
        Serial.print("  xd2_n: ");
        Serial.print(xd2_n);
        Serial.print("  xd3_n: ");
        Serial.print(xd3_n);
        Serial.print("  status gripper:  ");
        Serial.println(gripper);


        // Restart Timer1 clock
        TCCR1B |= savePrescale;  

        flag = false; 
        flag_qh1 = false; 
        flag_qh2 = false; 
        flag_qh3 = false; 
    }
}
void loop() {
    delay(5);

    if (!run1 && !run2 && !run3 && !flag) {
        flag = true;
        savePrescale = TCCR1B & (0b111 << CS10);
        TCCR1B &= ~(0b111 << CS10);
        Serial.println("Done");
        if (gripper != 0){
      //Serial.println("OK");
      digitalWrite(GRIPPER,0);
      }
      // else {Serial.println("NO OK");}
      else
    { digitalWrite(GRIPPER,1);}
    }

}