AStar$py.class                                                                                      0000600 0000000 0000000 00000035634 11775062032 012240  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   18 f$0 R(Lorg/python/core/PyFrame;Lorg/python/core/ThreadState;)Lorg/python/core/PyObject; org/python/core/PyFrame  setline (I)V  
   java 	 org/python/core/imp  	importOne H(Ljava/lang/String;Lorg/python/core/PyFrame;I)Lorg/python/core/PyObject;  
   setlocal /(Ljava/lang/String;Lorg/python/core/PyObject;)V  
   sys  array  	importAll /(Ljava/lang/String;Lorg/python/core/PyFrame;I)V  
   math  java.awt  configs.noErrors ! importOneAs # 
  $ cfg & #com.lib.udacity.simulator.abstracts ( com.lib.udacity.simulator.view * com.lib.udacity.simulator , com.lib.controller . com.lib.udacity 0 com.lib.util 2 AStar$py 4 _1 Lorg/python/core/PyInteger; 6 7	 5 8 
ITERATIONS : org/python/core/PyObject < _2 > 7	 5 ? _3 A 7	 5 B _4 D 7	 5 E org/python/core/PyList G <init> ([Lorg/python/core/PyObject;)V I J
 H K java/util/Arrays M fill (([Ljava/lang/Object;Ljava/lang/Object;)V O P
 N Q ANGLES S _5 U 7	 5 V _6 X 7	 5 Y SPEED [ _7 ] 7	 5 ^ _8 ` 7	 5 a COSTS c _9 e 7	 5 f _10 h 7	 5 i GOAL k None m getname .(Ljava/lang/String;)Lorg/python/core/PyObject; o p
  q 
SIMULATION s FRAME u LISTENER w org/python/core/Py y EmptyObjects [Lorg/python/core/PyObject; { |	 z } org/python/core/PyFunction  	f_globals Lorg/python/core/PyObject; � �	  � initWorld$1 (ILorg/python/core/PyObject;)V  �
  � range � 	getglobal � p
  � 
worldWidth � __getattr__ � p
 = � worldSpacing � _div 6(Lorg/python/core/PyObject;)Lorg/python/core/PyObject; � �
 = � __call__ S(Lorg/python/core/ThreadState;Lorg/python/core/PyObject;)Lorg/python/core/PyObject; � �
 = � __iter__ ()Lorg/python/core/PyObject; � �
 = � worldHeight � getlocal (I)Lorg/python/core/PyObject; � �
  � append � __iternext__ � �
 = � f_lasti I � �	  � Lorg/python/core/PyCode; � �	 5 � j(Lorg/python/core/PyObject;[Lorg/python/core/PyObject;Lorg/python/core/PyCode;Lorg/python/core/PyObject;)V I �
 � � 	initWorld � 
buildMap$2 int � __getitem__ � �
 = � _add � �
 = � __setitem__ 7(Lorg/python/core/PyObject;Lorg/python/core/PyObject;)V � �
 = � � �	 5 � buildMap � 	drawMap$3 setColor � Color � red � _eq � �
 = � __nonzero__ ()Z � �
 = � drawRect � _mul � �
 = � �(Lorg/python/core/ThreadState;Lorg/python/core/PyObject;Lorg/python/core/PyObject;Lorg/python/core/PyObject;Lorg/python/core/PyObject;)Lorg/python/core/PyObject; � �
 = � m �	 z � � �	 5 � drawMap � heuristic$4 getGoalX � 9(Lorg/python/core/ThreadState;)Lorg/python/core/PyObject; � �
 = � getGoalY � sqrt � _sub � �
 = � _11 � 7	 5 � _pow � �
 = � � �	 5 � 	heuristic � 	collide$5 _12 � 7	 5 � _ge  �
 = _lt �
 = True False � �	 5
 collide collideCheck$6 BicycleModel getPos _13 Lorg/python/core/PyFloat;	 5 	carLength T(Lorg/python/core/ThreadState;[Lorg/python/core/PyObject;)Lorg/python/core/PyObject; �
 = unpackSequence 8(Lorg/python/core/PyObject;I)[Lorg/python/core/PyObject;
 z m(Lorg/python/core/ThreadState;Lorg/python/core/PyObject;Lorg/python/core/PyObject;)Lorg/python/core/PyObject; � 
 =! makeException 9(Lorg/python/core/PyObject;)Lorg/python/core/PyException;#$
 z% org/python/core/PyTuple'
( K �	 5* collideCheck, expand$7 _14/ 7	 50 _152 7	 53 len5 setException M(Ljava/lang/Throwable;Lorg/python/core/PyFrame;)Lorg/python/core/PyException;78
 z9 java/lang/Throwable; _in= �
 => __not__@ �
 =A. �	 5C expandE isInRange$8G �	 5H 	isInRangeJ run$9 sortM popO extendQ setPathS repaintU _16W 7	 5X �(Lorg/python/core/ThreadState;Lorg/python/core/PyObject;Lorg/python/core/PyObject;Lorg/python/core/PyObject;)Lorg/python/core/PyObject; �Z
 =[ _17 Lorg/python/core/PyString;]^	 5_ println (Lorg/python/core/PyObject;)Vab
 zc _18e^	 5fL �	 5h runj checkCollision$10 _19m 7	 5nl �	 5p checkCollisionr (Ljava/lang/String;)V org/python/core/PyFunctionTableu ()V Iw
vx self 
LAStar$py;z{	 5| 
newInteger (I)Lorg/python/core/PyInteger;~
 z� FAIL� org/python/core/PyString� fromInterned .(Ljava/lang/String;)Lorg/python/core/PyString;��
�� _0 ;/mnt/drive1/Downloads/kubuntu/Downloads/CarSim_0.3/AStar.py��^	 5� DONE�?�z�G�{ newFloat (D)Lorg/python/core/PyFloat;��
 z� java/lang/String� <module>� newCode �(I[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IZZLorg/python/core/PyFunctionTable;I[Ljava/lang/String;[Ljava/lang/String;II)Lorg/python/core/PyCode;��
 z�  �	 5� w� i� col� j� pos� dots� d� x� y� g� p� GoalX� GoalY� map� ww� wh� dx� dy� nx� ny� x2� y2� a2� fact� todo� step� donel� first� cost� a� c2� next� p1� p2� angle� start� found� done� tmp� inst� world� n� getMain ()Lorg/python/core/PyCode; main ([Ljava/lang/String;)V 4 It
 5���
 5� org/python/core/CodeLoader� createSimpleBootstrap 9(Lorg/python/core/PyCode;)Lorg/python/core/CodeBootstrap; 
� runMain 5(Lorg/python/core/CodeBootstrap;[Ljava/lang/String;)V
 z getCodeBootstrap !()Lorg/python/core/CodeBootstrap; #org/python/core/PyRunnableBootstrap
 )getFilenameConstructorReflectionBootstrap 2(Ljava/lang/Class;)Lorg/python/core/CodeBootstrap;
 call_function S(ILorg/python/core/PyFrame;Lorg/python/core/ThreadState;)Lorg/python/core/PyObject;  
 5 � 
 5 � 
 5 � 
 5 � 
 5 � 
 5 
 5. 
 5 G 
 5"L 
 5$l 
 5& org/python/core/PyRunnable(  Lorg/python/compiler/APIVersion; value     Lorg/python/compiler/MTime;  7�` org/python/core/ThreadState0 | Code LineNumberTable StackMap 
SourceFile RuntimeVisibleAnnotations ! 5v )   z{    h 7    e 7    6 7    ` 7    D 7   e^    X 7   �^    ] 7   m 7    U 7    � 7   ]^   / 7   2 7   W 7    � 7    > 7    A 7        �    � �    � �    � �    � �    � �    �   . �   G �   L �   l �       3      �+� 
+� N+
-� N+� +� N+-� N+� +� +� +� +�  +� +� "+� %N+'-� N+� )+� +� ++� +	� -+� +
� /+� +� 1+� +� 3+� +� � 9N+;-� N+� � =N� @-__S� C-__S� F-__S� C-__S� HY-� L-� RN+T-� N+� � =N� W-__S� W-__S� W-__S� Z-__S� HY-� L-� RN+\-� N+� � =N� _-__S� @-__S� _-__S� b-__S� HY-� L-� RN+d-� N+� � =N� g-__S� j-__S� HY-� L-� RN+l-� N+� +n� rN+t-� N+� +n� rN+v-� N+� +n� rN+x-� N+� � ~N� �Y+� �-� �� �N+�-� N+ � � ~N� �Y+� �-� �� �N+�-� N+'� � ~N� �Y+� �-� �� �N+�-� N+1� � ~N� �Y+� �-� �� �N+�-� N+;� � ~N� �Y+� �-�� �N+-� N+M� � =N� @-__S� �Y+� �-�+� �N+--� N+V� � =N+	� r-__S� �Y+� �-�D� �N+F-� N+q� � ~N� �Y+� �-�I� �N+K-� N+w� � ~N� �Y+� �-�i� �N+k-� N+ �� � ~N� �Y+� �-�q� �N+s-� N+� �� �   4   z                            	   
                                        '   1   ;   M   V   q   w   �  �  3  �    +� � ~N� HY-� L-� RN+-� �N+� +�� �,+'� ��� �+'� ��� �� �� �� �N� �+� �+� � ~:� HY� L� R:+� �:+� +�� �,+'� ��� �+'� ��� �� �� �� �:� "+� �+� +� ��� �,� C� �W+� � �:���+� +� ��� �,+� �� �W+� -� �:��I+� +� �N+� �-�   4   & 	                           5   \  P  5 1 = =   �  5 1 = = = =   �  5 1 = = =   �  5 1 =    �  3  C     �+!� +� �� �N� �+� �+"� +�� �,+� �� C� �+� �� C� �� �+'� ��� �� �� �:+� �:+#� +�� �,+� �� @� �+� �� @� �� �+'� ��� �� �� �:+� �:+$� � @:+� �+� �� �+� �� �:+!� -� �:��@+%� +� �N+� �-�   4       !   "   #   $   !   %5   )    5 1 = =   �  5 1 =    �  3  �    >+(� +� �˶ �,+Ͷ �϶ �� �W+)� +�� �,+'� ��� �+'� ��� �� �� �� �N� �+� �+*� +�� �,+'� ��� �+'� ��� �� �� �� �:� �+� �++� +� �+� �� �+� �� �:� @_� �:� ֙ W+,� +� �ض �,+� �+'� ��� �� �+� �+'� ��� �� �+'� ��� �+'� ��� �� �W� +*� � �:��g+)� -� �:��+� �� �   4       (   )   *   +   ,   *   )5   \  P  5 1 = =   �  5 1 = = = =    5 1 = = =  $  5 1 =    �  3   �     �+2� +t� �� �,� �N+-� �N+3� +t� �� �,� �N+-� �N+4� +� �N+l� �� C-� �N+5� +� �N+l� �� @-� �N+9� +� �,+� �� C� �+l� �� C� �� � �� �+� �� @� �+l� �� @� �� � �� �� �� �N+� �-�   4       2   3   4   5   9  �  3  -    D+<� +�� �,+� �� C� �+'� ��� �� �� �N+-� �N+=� +�� �,+� �� @� �+'� ��� �� �� �N+-� �N+>� +'� ��� �+'� ��� �� �N+-� �N+?� +'� ��� �+'� ��� �� �N+-� �N+A� +�� �,� �� �� �N�Q+� �+B� +�� �,� �� �� �:�+� �+C� +� �+� �� �� �� �:+� �:+D� +� �+� �� �� �� �:+	� �:+E� +� �:+� �_�:Y� ֚ RW+� �:� C_�:Y� ֚ 6W+	� �:+� �_�:Y� ֚ W+	� �:� C_�:� ֙ � K+H� +� �+� �� �+	� �� �:� @_� �:� ֙ +I� +� �:+� ��+B� � �:���+A� -� �:���+K� +	� �:+� ��   4   :    <   =   >   ?   A   B   C   D   E   H   I   B   A   K5   �  �  5 1 = =   �  5 1 = = = =  �  5 1 = = = =  =�  5 1 = = = =  
  5 1 = = =    5 1 =     3      �+N� +�� �,+;� �� �� �N�>+� �+O� +� �� �,� =:+� �__S+� �__S+� �__S+T� �+� �� �__S+� �+\� �+� �� �� �__S�__S+'� �� �__S�:�:2:+� �:2:+� �:2:+� �::+Q� +� �,� =:+� �__S+� �__S� HY� L� R+� ��":+� �_� �:� ֙ +R� +n� ��&�+N� -� �:���+T� � =N+� �-__S+� �-__S+� �-__S�(Y-�)-� RN+� �-�   4       N   O   Q   R   N   T5   )    5 1 = =  X  5 1 =   .  3  �    �+W� +� ��1� �N+-� �N+X� +� �� @� �N+-� �N+Y� +� �� �� �N+-� �N+Z� +� ��4� �N+-� �N+\� +�� �,+6� �,+T� �� �� �� �N�+	� �+]� +� �:+
� �:+^� +� �:+� �:+_� +� �:+� �:+b� +-� �,� =:+
� �__S+� �__S+� �__S+	� �__S+� �__S�:�:2:+
� �:2:+� �:2:+� �::� +�::�%  �  �+f� +� �+d� �+	� �� �� �:+� �:+g� +� �:+� �_� �:� ֙ �+h� � =:+� �+�� �,� =:+
� �__S+� �__S� HY� L� R� �� �__S+
� �__S+� �__S+� �__S+� �__S+n� �__S+n� �__S+	� �__S� HY� L� R:+� �:� �+j� � =:+� �+�� �,� =:+
� �__S+� �__S� HY� L� R� �� �__S+
� �__S+� �__S+� �__S+� �__S+n� �__S+� �__S+	� �__S� HY� L� R:+� �:+l� +� �:+� �_�?:�B� ֙ !+m� +� ��� �,+� �� �W� +\� -� �:���+o� +� �N+� �-�  �z}< 4   F    W   X   Y   Z   \   ]   ^   _   b   f   g   h   j   l   m   \   o5   �  �  5 1 = =  }  5 1 = = <�   <�   <�  5 1 = =2  �  5 1 = =2  e  5 1 = =2  �  5 1 =   G  3   �     �+r� +� �,+� �� C� �+� �� C� �� � �� �+� �� @� �+� �� @� �� � �� �� �� �N+� �-_�N� ֙ +s� +� �N+� �-�+u� +	� �N+� �-�   4       r   s   u5     y  5 1   L  3  @    =+x� � ~N� HY-� L-� RN+-� �N+y� � =N+�� �,+� �� �-__S+� �� C� �-__S+� �� @� �-__S+� �-__S� C-__S+n� �-__S+n� �-__S� @-__S� HY-� L-� RN+-� �N+z� +F� �,� =N� ~:� HY� L� R-__S+� �-__S+� �-__S+� �-__S+� �-__S-�N+-� �N+|� +	� �N+-� �N+}� +	� �N+-� �N�B+� +6� �,+� �� �N� C-_� �N� ֙ + �� +� �N+-� �N� + �� +� �N� �,� �W+ �� +� �P� �,� C� �N+-� �N+ �� +� ��� �,+� �� �W+ �� +� �� C� �N+	-� �N+ �� +� �� @� �N+
-� �N+ �� +� �� �� �N+-� �N+ �� +� ��4� �N+-� �N+ �� � ~N� HY-� L-� RN+-� �N+ �� +� �R� �,+� �� �W+ �� +� �R� �,+� �� �W+ �� +x� �T� �,+� �� �W+ �� +v� �V� �,� �W+ �� +K� �,� =N+
� �-__S+� �-__S� HY-� L-� R+l� ��Y�\� ֙ ++ �� +� �N+-� �N+ �� �`�d� 3+ �� +F� �,+� �+� �+� �+� �� �N+-� �N+~� +� �N+	� �-_� �NY� ֙ W+� �N+	� �-_� �N� ֚��+ �� +� �N+� �-_� �N� ֙ + �� �g�d� + �� +� �R� �,+� �� �W+ �� � =N+� �-__S+� �-__S�(Y-�)-� RN+� �-�   4   r    x   y   z   |   }      �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   ~   �   �   �   �5   y <  5 12  ~  5 12  K  5 122  {  5 12  �  5 12  =�  5 12   l  3  �    H+ �� +� �N+n� �-_� �N� ֙ + �� +� �N+� �-�+ �� +�� �,+6� �,+� �� �� �� �:� �+� �+ �� +-� �,� =:+� �+� �� �� @� �__S+� �+� �� �� �� �__S+� �+� �� ��4� �__S+� �+� �� ��o� �__S+� �__S� F__S�W� %+�::+ �� +� �N+� �-�  �  �+ �� � �:��0+ �� +	� �N+� �-�  f � �< 4       �   �   �   �   �   �   �5   f  6  5 1   _  5 1 = =   �  5 1 = = <   <   <  5 1 =    It 3  �    �*�y*�}r��� j��� g��� 9���� b��� F����g���� Z�����
��� _���od��� W��� �����`���1���42���Y��� ���� @��� C������M,+��} ������M,�S,�S,�S,�S,+��}��� ���M,�S,�S,�S,�S,�S,�S,+� �}��� ���M,�S,�S,�S,�S,+�'�}��� ���M,�S,�S,�S,+�1�}��� �
��M,�S,�S,�S,�S,�S,�S,�S,�S,�S,	�S,+;�}�����M,�S,�S,�S,�S,�S,�S,�S,+-M�}���+��M,�S,�S,�S,�S,�S,�S,�S,�S,�S,	�S,
�S,�S,�S,�S,�S,+FV�}���D��M,�S,�S,�S,+Kq�}���I��M,�S,�S,�S,�S,�S,�S,�S,�S,�S,	�S,
�S,�S,�S,�S,+kw�}	���i��M,�S,�S,�S,+s ��}
���q�     �� 3        ���     	�� 3   !     � 5Y������*��     		 3         5��      3  �     n*,-�      h       
   <   @   D   H   L   P   T   X   \   `   d���������������!��#��%��'��   5  .  @  5 1  5 1 D  5 1  5 1 H  5 1  5 1 L  5 1  5 1 P  5 1  5 1 T  5 1  5 1 X  5 1  5 1 \  5 1  5 1 `  5 1  5 1 d  5 1  5 1 h  5 1  5 1 l  5 1  5 1 6   �7    * +I,- +J.                                                                                                    build.xml                                                                                           0000600 0000000 0000000 00000002355 11761075204 011375  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   <project name="CarSim_0.3" default="dist" basedir=".">
    <description>
        build file for Car Simulator ver 0.3 
    </description>
  <!-- set global properties for this build -->
  <property name="src" location="./src"/>
  <property name="build" location="./src"/>
  <property name="dist"  location="./src"/>

  <target name="init">
    <!-- Create the time stamp -->
    <tstamp/>
    <!-- Create the build directory structure used by compile -->
    <mkdir dir="${build}"/>
  </target>

  <target name="compile" depends="init"
        description="compile the source " >
    <!-- Compile the java code from ${src} into ${build} -->
    <javac srcdir="${src}" destdir="${build}" includeantruntime="false"/>
  </target>

  <target name="dist" depends="compile"
        description="generate the distribution" >
    <!-- Create the distribution directory -->
    <mkdir dir="${dist}/lib"/>

    <!-- Put everything in ${build} into the MyProject-${DSTAMP}.jar file -->
    <jar jarfile="${dist}/lib/MyProject-${DSTAMP}.jar" basedir="${build}"/>
  </target>

  <target name="clean"
        description="clean up" >
    <!-- Delete the ${build} and ${dist} directory trees -->
    <delete dir="${build}"/>
    <delete dir="${dist}"/>
  </target>
</project>
                                                                                                                                                                                                                                                                                   Car.py                                                                                              0000600 0000000 0000000 00000005734 11757604700 010643  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   import java
import sys

from math import *
from java.awt import *

import configs.noErrors as cfg
import AStar as astar
from com.lib.udacity.simulator.abstracts import *
from com.lib.udacity.simulator.view import *
from com.lib.udacity.simulator import *
from com.lib.controller import *
from com.lib.udacity import *
from com.lib.util import *

def drawNode(g, node):
    x  = px = node[1]
    y  = py = node[2]
    an = node[3]
    for j in range(astar.ITERATIONS):
        x, y, an = BicycleModel.getPos(x, y, an, astar.ANGLES[node[7]], -astar.SPEED[node[7]], 0.02, cfg.carLength)
        g.drawLine(int(px), int(py), int(x), int(y))
        px = x
        py = y
  
def drawPath(g, node):
    drawNode(g, node)
    if node[6] != None:
        drawPath(g, node[6])
    
def drawTree(g, nodes):
    for n in nodes:
       drawNode(g, n)

def getDrivePath(node):
    p = [node]
    while node[6] != None:
        node = node[6]
        p.append(node)
    return p

class MyListener(SimulationListener):  
    def init(self, ctrl, background):
        print "MyListener init"
        self.dots = [[0,0]]
        self.scanPos = [0,0]
        self.cnt = 0
        self.car = ctrl
        self.world = astar.initWorld()        
        self.inst = None
        self.path = None
        self.lastNode = None
        
    def onUpdate(self, dt):
        if self.cnt>=astar.ITERATIONS:
            if self.inst != None and len(self.inst) > 0:
                cur = self.inst.pop()
                self.car.setSteer(astar.ANGLES[cur[7]])
                self.car.setSpeed(astar.SPEED[cur[7]])
                self.cnt = 0
            else:
                self.car.setSteer(0)
                self.car.setSpeed(0)
        self.cnt += 1
    
    def onPaint(self, g):
        astar.drawMap(self.world, g)
        if self.path != None:
            pos = self.car.getPos()
            g.setColor(Color.orange)
            drawTree(g, self.path)
        
        if self.lastNode != None:
            g.setColor(Color.green)
            g.setStroke(BasicStroke(2))
            drawPath(g, self.lastNode)
            g.setStroke(BasicStroke(1))
        
    def onGPS(self, pos):
        astar = 1
        
    def onCamera(self, img):
        astar = 1
        
    def onScanner(self, dots):
        self.world = astar.buildMap(self.world, self.car.getPos(), dots)
        if astar.checkCollision(self.inst, self.world) == True:
            self.path, self.lastNode = astar.run(self.world, self.car.getPos(), self.car.getAngle())
            self.inst = getDrivePath(self.lastNode)
            self.cnt = astar.ITERATIONS
 
    def setPath(self, p):
        self.path = p
              
listener = MyListener()      
s = Simulation()
s.loadConfig("configs/"+cfg.fileName)
s.setListener(listener)
v = SimulationFrame(s)
s.setGoalX(770)
s.setGoalY(570)
astar.SIMULATION = s
astar.FRAME = v
astar.LISTENER = listener
s.start()
v.setVisible(1)
                                    configs/                                                                                            0000700 0000000 0000000 00000000000 11762166563 011207  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   configs/.directory                                                                                  0000600 0000000 0000000 00000000116 11741252660 013203  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   [Dolphin]
Timestamp=2012,4,11,15,28,8
Version=2

[Settings]
ShowDotFiles=true
                                                                                                                                                                                                                                                                                                                                                                                                                                                  configs/noErrors$py.class                                                                           0000600 0000000 0000000 00000007303 11775062032 014457  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   1 � f$0 R(Lorg/python/core/PyFrame;Lorg/python/core/ThreadState;)Lorg/python/core/PyObject; org/python/core/PyFrame  setline (I)V  
   configs/noErrors$py 	 _1 Lorg/python/core/PyString;  	 
  fileName  setlocal /(Ljava/lang/String;Lorg/python/core/PyObject;)V  
   _2  	 
  mapFile  _3 Lorg/python/core/PyInteger;  	 
  carSpeedSensorError  carGyroSensorError   carSteerError " carSpeedError $ _4 & 	 
 ' carMaxSpeed ) _5 + 	 
 , carMaxSteer . _6 0 	 
 1 	carStartX 3 _7 5 	 
 6 	carStartY 8 _8 Lorg/python/core/PyFloat; : ;	 
 < carStartAngle > 	carLength @ 	carSteerT B 	carSpeedT D _9 F 	 
 G worldSpacing I _10 K 	 
 L 
worldWidth N _11 P 	 
 Q worldHeight S gpsSensorNoise U cameraImageNoise W cameraUpdate Y gpsSensorUpdate [ laserScannerUpdate ] _12 _ 	 
 ` laserScannerRange b errorUpdateTime d f_lasti I f g	  h org/python/core/Py j None Lorg/python/core/PyObject; l m	 k n <init> (Ljava/lang/String;)V org/python/core/PyFunctionTable r ()V p t
 s u self Lconfigs/noErrors$py; w x	 
 y 
newInteger (I)Lorg/python/core/PyInteger; { |
 k } _0 F/mnt/drive1/Downloads/kubuntu/Downloads/CarSim_0.3/configs/noErrors.py � org/python/core/PyString � fromInterned .(Ljava/lang/String;)Lorg/python/core/PyString; � �
 � �  	 
 � noErrors.py �?�!���o newFloat (D)Lorg/python/core/PyFloat; � �
 k � testMap3 � Lorg/python/core/PyCode; java/lang/String � <module> � newCode �(I[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IZZLorg/python/core/PyFunctionTable;I[Ljava/lang/String;[Ljava/lang/String;II)Lorg/python/core/PyCode; � �
 k �  �	 
 � getMain ()Lorg/python/core/PyCode; main ([Ljava/lang/String;)V 	 p q
 
 � � �
 
 � org/python/core/CodeLoader � createSimpleBootstrap 9(Lorg/python/core/PyCode;)Lorg/python/core/CodeBootstrap; � �
 � � runMain 5(Lorg/python/core/CodeBootstrap;[Ljava/lang/String;)V � �
 k � getCodeBootstrap !()Lorg/python/core/CodeBootstrap; #org/python/core/PyRunnableBootstrap � )getFilenameConstructorReflectionBootstrap 2(Ljava/lang/Class;)Lorg/python/core/CodeBootstrap; � �
 � � call_function S(ILorg/python/core/PyFrame;Lorg/python/core/ThreadState;)Lorg/python/core/PyObject;  
 
 � org/python/core/PyRunnable �  Lorg/python/compiler/APIVersion; value     Lorg/python/compiler/MTime;  7�B[� org/python/core/ThreadState � Code LineNumberTable StackMap 
SourceFile RuntimeVisibleAnnotations ! 
 s  �   w x    K     _     5     F     0          &          P     : ;    +                �        �  C    �+� � N+-� N+� � N+-� N+� � N+-� N+� � N+!-� N+
� � N+#-� N+� � N+%-� N+� � (N+*-� N+� � -N+/-� N+� � 2N+4-� N+� � 7N+9-� N+� � =N+?-� N+� � (N+A-� N+� � N+C-� N+� � N+E-� N+� � HN+J-� N+� � MN+O-� N+� � RN+T-� N+"� � N+V-� N+%� � N+X-� N+(� � HN+Z-� N+)� � HN+\-� N+*� � HN+^-� N++� � aN+c-� N+.� � N+e-� N+� i� o�    �   b                
                                       "   %   (   )   *   +   .  p q  �   �     �*� v*� z � ~� M ȸ ~� aP� ~� 7
� ~� H7� ~� 2�� �� �d� ~� (�� �� X� ~� R �� �� =� ~� -� ~� �� �� � �M,+�� z � �� ��      � �  �        � ��     	 � �  �         � 
Y�� �� �� �*� ��     	 � �  �         
� ��      � �  �   d     *,-�                 � ���    �   4    
  �  
  �   
  �  
  �  �    � �     �  �I � �  �J �                                                                                                                                                                                                                                                                                                                             configs/noErrors.py                                                                                 0000600 0000000 0000000 00000001472 11757605330 013372  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   #Filename for easy use
fileName="noErrors.py"
mapFile="testMap3"

#Variance for return values
carSpeedSensorError=0
carGyroSensorError=0

#Variance for calculation
carSteerError=0
carSpeedError=0

#Car Settings
carMaxSpeed=100
carMaxSteer=1
carStartX=55
carStartY=80
carStartAngle=1.57075
#carStartX=400
#carStartY=100
#carStartAngle=0
carLength=100

#First order Lag, T=0->no Lag
carSteerT=0
carSpeedT=0

#World Settings
worldSpacing=10
worldWidth=800
worldHeight=600

#Variance and for GPS
gpsSensorNoise=0

#Probability of wrong Pixel given back
cameraImageNoise=0

#50/update = freq (int only)
cameraUpdate=10
gpsSensorUpdate=10
laserScannerUpdate=10
laserScannerRange=200

#every errorUpdateTime (in sec) new random values for Calculation are generated
errorUpdateTime = 0

                                                                                                                                                                                                      configs/noErrors.py~                                                                                0000600 0000000 0000000 00000001472 11757576430 013600  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   #Filename for easy use
fileName="noErrors.py"
mapFile="testMap4"

#Variance for return values
carSpeedSensorError=0
carGyroSensorError=0

#Variance for calculation
carSteerError=0
carSpeedError=0

#Car Settings
carMaxSpeed=100
carMaxSteer=1
carStartX=55
carStartY=80
carStartAngle=1.57075
#carStartX=400
#carStartY=100
#carStartAngle=0
carLength=100

#First order Lag, T=0->no Lag
carSteerT=0
carSpeedT=0

#World Settings
worldSpacing=10
worldWidth=800
worldHeight=600

#Variance and for GPS
gpsSensorNoise=0

#Probability of wrong Pixel given back
cameraImageNoise=0

#50/update = freq (int only)
cameraUpdate=10
gpsSensorUpdate=10
laserScannerUpdate=10
laserScannerRange=200

#every errorUpdateTime (in sec) new random values for Calculation are generated
errorUpdateTime = 0

                                                                                                                                                                                                      configs/test$py.class                                                                               0000600 0000000 0000000 00000006223 11741257332 013627  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����  - � Code f$0 5(Lorg/python/core/PyFrame;)Lorg/python/core/PyObject; org/python/core/PyFrame  	setglobal /(Ljava/lang/String;Lorg/python/core/PyObject;)V  
   __file__ 
 configs/test$py  _0 Lorg/python/core/PyString;  	   LineNumberTable setline (I)V  
   _1  	   fileName  setlocal  
   _2  	    mapFile " _3 Lorg/python/core/PyInteger; $ %	  & carSpeedSensorError ( _4 * %	  + carGyroSensorError - carSteerError / carSpeedError 1 _5 3 %	  4 carMaxSpeed 6 _6 8 %	  9 carMaxSteer ; _7 = %	  > 	carStartX @ _8 B %	  C 	carStartY E _9 Lorg/python/core/PyFloat; G H	  I org/python/core/PyObject K __neg__ ()Lorg/python/core/PyObject; M N
 L O carStartAngle Q 	carLength S 	carSteerT U 	carSpeedT W _10 Y %	  Z worldSpacing \ _11 ^ %	  _ 
worldWidth a _12 c %	  d worldHeight f gpsSensorNoise h cameraImageNoise j cameraUpdate l gpsSensorUpdate n laserScannerUpdate p _13 r %	  s laserScannerRange u errorUpdateTime w f_lasti I y z	  { org/python/core/Py } None Lorg/python/core/PyObject;  �	 ~ � <init> (Ljava/lang/String;)V org/python/core/PyFunctionTable � ()V � �
 � � self Lconfigs/test$py; � �	  � 
newInteger (I)Lorg/python/core/PyInteger; � �
 ~ � 3/home/greeshma/Downloads/CarSim_0.3/configs/test.py � 	newString .(Ljava/lang/String;)Lorg/python/core/PyString; � �
 ~ � testMap � noErrors.py �?�!���o newFloat (D)Lorg/python/core/PyFloat; � �
 ~ � Lorg/python/core/PyCode; java/lang/String � ? � newCode �(I[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IZZLorg/python/core/PyFunctionTable;I[Ljava/lang/String;[Ljava/lang/String;II)Lorg/python/core/PyCode; � �
 ~ �  �	  � getMain ()Lorg/python/core/PyCode; main ([Ljava/lang/String;)V  � �
  � runMain 2(Lorg/python/core/PyRunnable;[Ljava/lang/String;)V � �
 ~ � call_function 6(ILorg/python/core/PyFrame;)Lorg/python/core/PyObject;  
  � org/python/core/PyRunnable � 
SourceFile org.python.APIVersion !  �  �   � �    ^ %    r %    B %    Y %    = %         3 %    $ %              c %    G H    8 %    * %     �          O    �+� � 	+� � M+,� M+� � !M+#,� M+� � 'M+),� M+� � ,M+.,� M+
� � ,M+0,� M+� � ,M+2,� M+� � 5M+7,� M+� � :M+<,� M+� � ?M+A,� M+� � DM+F,� M+� � J� PM+R,� M+� � 5M+T,� M+� � ,M+V,� M+� � ,M+X,� M+� � [M+],� M+� � `M+b,� M+� � eM+g,� M+"� � 'M+i,� M+%� � ,M+k,� M+(� � [M+m,� M+)� � [M+o,� M+*� � [M+q,� M++� � tM+v,� M+.� � ,M+x,� M+� |� ��       b  	    -  @  S 
 f  y  �  �  �  �  �  �   ' : M "` %s (� )� *� +� .  � �     �     �*� �*� � � �� ` ȸ �� tP� �� D
� �� [7� �� ?�� �� d� �� 5� �� '�� �� !�� �� X� �� e �� �� J� �� :� �� ,� �M,+�� �� �� ��      � �          � ��     	 � �          � Y�� �*� ��      � �     &     *,�              � ���      �    � �                                                                                                                                                                                                                                                                                                                                                                                   configs/test.py                                                                                     0000600 0000000 0000000 00000001470 11730372126 012531  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   #Filename for easy use
fileName="noErrors.py"
mapFile="testMap"

#Variance for return values
carSpeedSensorError=30
carGyroSensorError=0

#Variance for calculation
carSteerError=0
carSpeedError=0

#Car Settings
carMaxSpeed=100
carMaxSteer=1
carStartX=55
carStartY=80
carStartAngle=-1.57075
#carStartX=400
#carStartY=100
#carStartAngle=0
carLength=100

#First order Lag, T=0->no Lag
carSteerT=0
carSpeedT=0

#World Settings
worldSpacing=10
worldWidth=800
worldHeight=600

#Variance and for GPS
gpsSensorNoise=30

#Probability of wrong Pixel given back
cameraImageNoise=0

#50/update = freq (int only)
cameraUpdate=10
gpsSensorUpdate=10
laserScannerUpdate=10
laserScannerRange=200

#every errorUpdateTime (in sec) new random values for Calculation are generated
errorUpdateTime = 0                                                                                                                                                                                                        configs/__init__$py.class                                                                           0000600 0000000 0000000 00000004016 11775062032 014403  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   1 ` f$0 R(Lorg/python/core/PyFrame;Lorg/python/core/ThreadState;)Lorg/python/core/PyObject; org/python/core/PyFrame  f_lasti I  	   org/python/core/Py 	 None Lorg/python/core/PyObject;  	 
  <init> (Ljava/lang/String;)V org/python/core/PyFunctionTable  ()V  
   self Lconfigs$py; 
configs$py   	   _0 Lorg/python/core/PyString; F/mnt/drive1/Downloads/kubuntu/Downloads/CarSim_0.3/configs/__init__.py  org/python/core/PyString   fromInterned .(Ljava/lang/String;)Lorg/python/core/PyString; " #
 ! $  	  & Lorg/python/core/PyCode; java/lang/String ) <module> + newCode �(I[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IZZLorg/python/core/PyFunctionTable;I[Ljava/lang/String;[Ljava/lang/String;II)Lorg/python/core/PyCode; - .
 
 /  (	  1 getMain ()Lorg/python/core/PyCode; main ([Ljava/lang/String;)V   
  8 3 4
  : org/python/core/CodeLoader < createSimpleBootstrap 9(Lorg/python/core/PyCode;)Lorg/python/core/CodeBootstrap; > ?
 = @ runMain 5(Lorg/python/core/CodeBootstrap;[Ljava/lang/String;)V B C
 
 D getCodeBootstrap !()Lorg/python/core/CodeBootstrap; #org/python/core/PyRunnableBootstrap H )getFilenameConstructorReflectionBootstrap 2(Ljava/lang/Class;)Lorg/python/core/CodeBootstrap; J K
 I L call_function S(ILorg/python/core/PyFrame;Lorg/python/core/ThreadState;)Lorg/python/core/PyObject;  
  P org/python/core/PyRunnable R  Lorg/python/compiler/APIVersion; value     Lorg/python/compiler/MTime;  5�|7� org/python/core/ThreadState Z Code StackMap 
SourceFile RuntimeVisibleAnnotations !    S              (        \        	+� � �         \   :     .*� *� � %� '� *M,+,�  � 0� 2�      3 4  \        � 2�     	 5 6  \         � Y7� 9� ;� A*� E�     	 F G  \         � M�      N O  \   d     *,-�                 � Q��    ]   4      [    [     [    [  ^     _     T  UI V W  UJ X                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  configs/__init__.py                                                                                 0000600 0000000 0000000 00000000000 11725115256 013300  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   img/                                                                                                0000700 0000000 0000000 00000000000 11762166563 010333  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   img/car.png                                                                                         0000600 0000000 0000000 00000035357 11724654610 011616  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   �PNG

   IHDR   -   d   M�>   	pHYs  �  ��o�d  9iCCPPhotoshop ICC profile  xڭ��J�P��EšV��p'QPl���I[� X�C��IC��$�ܪ}G�.�>����������!Hp�o����p��bם�Q�A�U��H����3L@'�R��: ��8�'>_ ϛv�i�7��Ti`lw�,Q�:� ƀ�S�0�I��(�rJA�o@I���0{��1�A�+���KPKґ:�jY�,K��$���(�� ��q��4Qu��? ��vӑkU��[�q=_��~� ��c��Cu�݅���\�/��-LO�l�
n6`��V�Pނ��³O�	�'    cHRM  z%  ��  ��  ��  R X  :�  o�Z�  90IDATx���gP\g�/�V�rFH rα����M�V��9#�@P�9Y%�HB���,�c�=�����-�Ǧ��C˞=w��뜺�~������O�׳��" �����~8!1aX|B����q�	�S�c���hY^Y�L���D��L�WrZ����E�S��,�t
%mZRb�Ԥ�ة��z֔丘)���q<F���O�d
y�����Ȉ��lzttlTNjF��LM�Pr��q�ibV���H����Q�!��8qRV?�����I��f�sS)1��I�9��8�����1����c��Q(��	��S��,f'�����D!�����'ӭ�'3�'����9�ԓ,E�I��v2W�~�V}�����ݙe�A7F��QEoaH�ۅ�,'�GMȥ����2��_A�gdK���JN��Ɗ&2u������[B_3�"��Y�5oU��lG��,�kA�k����\#�Z g�Y����2�s~{�gܶ�O��>e/�{�i�{ʯ=+�&��x�LVv�L��7���N��K��B��I�Ph��<zɬ�����b��Ny'Z���du��.}(��3$\�:$^�0$oOR��IZS~�
�?���_�O�Ұ�K�~,	����E����O��ܨ4G8���(c���=���f��Q(��ii�s�i�t[ '�lv��jn��v�K� ��W'��ߑ��,� kYXbr��X ��Y�.��̅�@k���������^0얩`�L����Y4��n���v�7��9OU�%�eR�o�Z���F�o�SRR����} 	��p�cY����w���w�|����i?����Z�f��#{�\d����gu8a�n�F����^6�K���d�|X��"w�T0MBn���Gn�X7�~�������o��f�jWWaC��3�oӲ��r��-:==}8���?�)�g0�񅆊�ݵE��v�y���(����kM(8k�:�Us��r!X���H��}��ڼ@]6�g����:��㑽drM��O�etÆ�mkz{���?�p[O�R��+C+�G�y�	�`�B��������tN
_T�h25JN-Z��j�����ٵ��Kv���k�����p���6�k���� ����19+g {��Wz!{�4�J��3S��x���Eβ�`.� �҉`�Ms�XHZ�д\7tpﾟ�N��ˡ���k���$��Y�B0�(���74�Ǜ�d�Ds�t-�"a�h�g����?��Ǯ��~9~�Cw�n+D�#����Hp7���1�u���C(@P���`�����`�GC(��<�%���l,�m��j�	�M�m<��ǡby.����>y���Μ�n׾u�
��TU6*�Il�\4��a��74����%XM�;h�s*+Y_oZ���/\:�u��n@�V.�[B!���H𷆁�5�M���L�zw6Dz6:&�&:::˽�\1�ec�Z6����m^�x�&��b"x�� ou�Y��'O��uu�r������7�b�r=��p�����H ���N��/���ڟ�`�_�w����<މ�[w�m[=��!��XwEB�#����l���@&�G8�o{Q؋���ƺi`���܎	`���m4�+Ɓ�>�S��A�1ܕ��[���p��>?rg;O����C�4�+������a�Lr�D���E@b���”���}��2�'K��v����'�e��m2���hH��B�7
�=��
g ��9��C�3��g��y����q*�맀�f<8�? �m�+ǀ�b���@�r,��ǃ��dkg`��ߏK�/��ɳhYQ�V,���z����+o���:�D鉇��eW��gl��cy���-&�wW.����=(�)�t_4�G�!�0��� O ��"��R��%�`w0��f����ۦ#w�4�n�����A�H�V�o�X�׌�`�X�׍o�h֏G�	.\?��;wp��qT/tA�*f��9�Gu}�3=�ۮ�sSI H��^nM��^�?����\��]�/���[�zz�Y��q,�#�����H�By$%׬p^�C�/ �]���	���`m��֩�l���������8�c!�8�M���<�M����-����q�ټeM6��&�U�}ߩ[��:N�F��  �e,�6���p���nZ_��]8г�'eМH��3�IP�H��x�G#!�0�ә��-�������o�,pwO{�tpvMg�D�֏�p�6�o�$�L�x�D��N�x�DHvL�x�DضŠmg֯Z��&�)n�a�w�%����D�=h�����$�$|�����vc	V�jE�e��Ӡ;C��L�gR�9�թ'b ;
�E.�T�uM
�� Ά`�7x�g��o:�{���{[>�x����`�DvM�h�$�vM�d�$��L�d�d��N��@j��P�D����֞}�m�t:�r׃NɌ�%|h���Ǽs��ˎ�P|��5��`�@��+��Th�$As:�SqPvF���M��&��X ���@�����;8����7��c Y;�@�w2�{'C�g2�{'A�w���Bq`�f@~d:��g��2�Yn���w���A��ס	�I HY�4oI�a��j��~���U�yp��`�B��
��Y0\�@>�sIPuŃ8���4?k��[qg ��|!>6���!8�����h�8H6�d�(�L���HL�t��N���t(� qt���P���(���6��}�^;(V�:�\��+�
E+����5��E�[P�� �=<خ3`�΀�j�W�a�������C{>�MX��>䧂 ��	?�Ó����gAtlD&B�y8��GA|h*ć�Azh:d��C~d:�f�8>��9P����4؎��j��r1��j}Ԡ����(�4O�
W&-�+��y���E����y�p�̅��	�u:��2a�J��r
��`���ڇ,x5�[l(�Cq&�3��������N�@r��C�!�:ҝ# =:�3!;>����	e�,�O΁��/4g|�?�ۉ@^�t[.ŽSm����;Ԅ�tA�P�:�h�=�WM���,��	��\(�'@~/y�Xp�d��M��;��&�r���g�h���[,�χ�8�� ��@vv.��� ;=��� �9�]#��	�i_�O͆��g�83곾�tͅ�\ �'f�v���n��wĆ�A����=h�,V$\q�u��U���_�i@�3'
��Qx����8{��ݦ�z�
KO�7Ra롢�y�_��y3ڋ�P_���b���P�����ss!?5�=�����S>Pvͅ��D�/����9�ݹ ��x!�ӳa;5�גݦ+Q�4�"s���N�A3ԉb�����^ڟk�[Y���](���O���|��e�u�	G/�^,7)p�fc��B�Y�mt�b����p���A})�K�P]
q���c!�?
���P]
q��E�/@{1�K��]��J��`>��D��J�;���Am�C*�dz�!����w�o&����~h�'u�7�D�#	�IP�P��>���ˀ�������ż.Կp��K��;��8h������讄Cs%�P���P����P��C}9����^	��J8�W#aꎃ�b,g`��6\
|���7h(�w�\��O����9i�����vh���0��Od({"C�c	��Q��AA_.��3`�����\Կ��z��*,7�`�I��;��Xn�@w#��h讄@}l2���9�]w��à�����a쎆�;֞X�D�r>�+n�E�w�m~�Jgj�ݤ�UQR���'��¿�~�Z�Y�}�D�S9�({&C�SJ�Q����l��e��!5/�x����;i����|+	曉0݌��'��X�GA{b:�GBw��[���D������8Xn��z'��1�]�u��i����f�A�h"���SOꮅ}];hZ�y#�>�C�s�^�P�\���R�>��	%�x(z�B�C*�({*A�}�(�ߣ�v��X�$�ܛSo"L��;=Ӄ����D{�a썇�v,��֛��48n&�v)���n݅��;fj�)&�ڃ�R��D릞2]���#�В/��|ԾҢ�U�*T������τ(~*@�#J�P�L���<�����ς�/���?�.�����M��7	��>P8
������ޯe��{o�w��O��v��`���]�z��6uP]�ڡ��=h�$L.��:m��u����_֣��4�6��#j>Ң���/(�����=���O9(x�@��l<�#�y�p=̂�a:l�a{@��j��'�t9 �~
�}d����k����KG��,8��v5�kanݕ���;|��5!��3rb��v�3���Խ6-��-�/¼74~lB�Gz��
�D�+9�_�P�\��'�<ࢰ���{�p�f�y�GO6�=4�z��ݦ��K��f
̗B`�E��,�e!�Q�f"�A&�d��a
��~:WB<����N�%pPm�鰚�4��IZ����~S�Z?���J�~^�����������wԾ1�zЀ��*ސ#�����m¸��26Tr��ǀ�1�z*�u�5�!jN�tY*�S��M��3�t�����D��>a��	�OY(�G���/̗纵7|�!�Tv|��j~?=r3	vc�YKo�7կ�C-���4��M_��c*��(<��}'�B1�<�"(�rHyR��<�2��&�"39�L�ƒ�����D�F "*i�H䅂抅pY
�}�0_�F��_�Q�R���������9ncw�;���A� �C�&~Eg�Ơ�ֻ��T����̊�/�0����χe��r��,�it�)���E�J�ȳ����
ee�(+o@iy-
K��,,��Y��Bm�PL��"���ب�Eb�L��� 0i6�A�/O���R��D�rllW�M=!�tc%zz�F���ⷆ��ދ���x���M�T��#!5Q�� '��fI�6�P�Ԅ��[����?щ��;���ql����݇U;wa鶭hٰ��P���-���� Si	V+r�r$Sh�������E(D�R�?�ˑQ�_t�n���l�i�J����c���Kº����)%*�%w^B��7'�	�Ȓ( �9`(�D���w�.ܺ��7������y[��=��r�N,޴M�֣�����Q��%��ha+
["�����a�����|�	*f��w�d$# �0
�!n㭠w�U��bUv���x�L�dI�9�ͨo�zYC��D�ya�w B��(U���P��T[���7����8{�*�����'���a�۳+�m��1�ԬX��e�P�ڊ��M��7�T]]E%4�PUTB[U}M-L�uP���� 07$�g��4�3�n��w�U��������<Z�������?H��ҙ>ŝ�	^��C�"Z$F�J��ya1lu�X�u�]��/b��S�v�(��ۏU�w`���h^�u+V�|�2�.�k~3�u0V�BSVEq)�E�B���+¼|�JJ!/� M�Ü�p����z(����N�5v�Q���pY�G���Wn�?_���m�%�P�����cnf6bbdp�v(��aoh��-[q��y�:��'N`��CX�k7�mނ���аj*��Pܺ��Ͱ��C_QeI9��:��u8�����X�4{�k��c����#���l;��L�A�;Ŏ�A���a2�wښ��o�8_������R?L��4b�bdp�v(�Ka�o�����8s[��ڽ�Ѿm;n؈�U�ikC��Ep55�R� ]E��H�
��;�2[�c0��Ճ���V��Z=�����!^,ż�U�_sߩ�FJ�|��i\g�o�P���m�C�k�/f�z�'���{������:4w���cǱ��$6}x��`��-X�f-���r�".X {c#U5 J� �+ �� �h]�G&�EA M�@�T�)��
%Bi�g$@�^���w��w����
v���-��)vD\q�c�հ�5�l�A�l:|�S�!�P�c�CQ\
sM-jږa����y�86<�;va��M�߱5mm(Y�
��&�k�)�����L�4��JR�r$�$���"�/B�@�X����hS�Z͇i��m��z�>��(�Yc0꩞�a��ʶ�Q�{z~��t
2*f�?#!��	�fE%0Uנ�u!ڷl���}��|�N,\��+W�j�b-X Gc#��� �K!r�m�![oD�J�T�	B1b�|D�8e���F8���²(����i�D�-�-�5���~o�E�m*��,!$o�vF��\
}�U3˝\0	��Y�" =d�
,���b��jP���֭ǆ}��~�>�ؾ�6lBÊ��\�EZ`oh���
��b�.0Mdit +$�$����d!����lP�cr���d9��,0j�A)�ũ�?k:���_@?%%�V ���F����ҟyk���"?������T��i~�յ(nmEs�jt�؉u{�b���X�q3�[[QZ߀��j8K�`(.�,�<�9z�TZ�I����� �ƀ_z|R��NCK�h*��l�v�^���E�(N�~�����O]�XB@*�ܩ~������!���%#�  �I	HȐc2C�_]e5���m�ـ��cՖ��j����2���!����bX�.�mN��&P�d�H�K��"��
�ɩ�����L:��e��H�lI�,��y�x��~�����;`�E[O@W%�	����N�G��vH@���4!�d#S�Ko����YSa	�%�p���U\��g��b'Ly6���M*8�H�J0<��lP�L�gg",���̉��_B��\$�%�ͥ@��
�.����!����Lܷ�VF��\��9�h����o9��S��s�JXڝ0�c"V䏠�x$��A�d���ӐA!�y�
�,�ñ��k���$p�¶��N.̫�p[A��B�N���NY2����c���Df��dD%� Y�f6�5b��dA�J��g��5���(+M?f�[�$ $�.Q/��{�����j�t(Ǭ�si*.� XvU�[�(<�GE���v4?�G�`�_��r���B���j�HQ6�C�S��Q���˅��,��Pp/��4دP`>�
��H����iΙ�,��y�YvBhY���p��O���߳]q{�=ϳ>-�'�������Q��T�o����R�~$G�EX�M-Z�\������q�_90��/�p�\��S����(y�E�C���(������p�!�z+	��XX��a���Phz��M�,��%�|� YC �N�|���x?�:�>%��v0ٌ\ R�8� ���=&��'�6(Y�k�-A�'Z�aB�
���?�{���Ĉ�Ԩ���݄��ʞ�P򔁢�T>�D��8v�X���^Lwb`ꍄ�v(�7����Uo(�π���n{�ޟ�~-ҔB�T(�KP8��I~4�w삸mrB��l3k#T���]���o4��C9&UW`G�f��Ά�����e>���a���h�T��7r�rP��
�e:��68v�a���(X�E¶�g����0���n(wB��m�?Է���9�^P\�
��9p�˄y�d��*�MR�?���=󉪒�Ug�0<LEi�рs���o��C9j�������"T�D�v4}nC��:������o�.L���x(OO��F	[��F���T�fC�3�[~�ݞ]���ꖧ�=���1�;��΄i�	d�*��
�rRuF��mJ9$ $aa�N{����1�[͇��l�5�V���cX�E5�?Sb�g&��Ԉ��W�@�� ĩP�� ��㠸0ʋ��=��Ph>qu*��ӡ�	�Mhn��� ]o wC`�ý0�B`��	�z#�$"s�Po'��/y�О��XQ���Πe� ��%)z�1����ou�$C96j�B�3X�ej?Sc��M��X{oTgGCyf����'�8?ʋ��4ĥ�P^���)P^��Zu��?��A/��Q0����0
���ט�&Q#�̀f��;�ZU��A���H Hʒt�������o���C��;p�I6}���ע�3=�_�a�e�h(ύq~<�����2����w��wZ������x?��h��t��j#�$j�p���R�^���?󑶎�.����y�D�r�܋����H�r����3����h��O5(`@m6��@y~�|q<��&Byy�W&Cyuʿ�ק����g�{�/����NwC`���(X������j"��uH��eB�[�.��Cs"򕤈�����siʳ%Y��.;���j:*b;4�^؁�gg����0�V�|B��I&t׼=��A\� ��$(/O�k$~E_��Z�3�[�Ck�@�Ц�(�������J,t��j�r���Ѹ��4��/y)���<���t��ˎ�俚�ˆ�.5��±g'��/����5o�=H���(.����Ow�C��W������ny�����~r�G���6�GCs���ЭV�"� �ˀq��]4����/upx����ۓ��W\O��j:!b��j]�C�c�_������~-��?ګ3��8�_�o�) ~��T�{&��������F��"`�?껾�\�n�1�8��Zw� ���l��.s����l�4�r��U��߬'C�B�[�q��~���b,��կ�p<H���'y&���Ay�V^���t�3<]��S���eӽX�G�����{}���:	��J�
�0ԸK^
�jN�>�Ŭ�*$��O�2�E���|L���r�W�Ce�2��߁�n�¯JQ�Z��$h�gCqe�{����+�č�i�����n������>���/�[�����z1R%J�
sa<�u���՞
P7P۵ų,�˓���z��7[�bHXj@y�2l�ۈ�_5c�_�P����������) �{���1D�L��xSߚ�[�����{�0���~�}Q�>���/��P_��&�2�E,���ů�ou���r�qm9�l2	 Id�,p�ʼ��B�]�%�[UeAe�b�����܈e�6��ǣ�z:z}*T7f@uc��YP�x{:�����-�����G���X%z��^P]��6R�"ıi�����*w�=�V�����4���'97��[�;�w4:��҄�7j�䏕h�k*��>J��/
��>Pv{���z��(̆��/4����0�E��k��`�۽hhoLqqxKb���`�WǺ�g&���0��BY��k=��S��+�{�]s�+=�t/^ӈ5k�����(@�ߚQ����8��ba����P�z����(hoυ�N �w�~��o9�s_,�����?J��n4tW�Aun22*g��o*�������H?���z�q
Ri�O���Ś����qߕ^����X����ce��ތߵ���"�}$B�+>J^��?@��q쏒`}� ˣX��� ��h��`x	C_�}�����^�������@��@' �;�0v�A{qT&��<�ٙH�$C�|�[�9�G��9��6i�P(L����2���[E��/��w�ZJ�t�J,R��O������j%�i¼�����ϋP�ā�G&=Ԣ��@�=	wx���`��SO��i�]O��j,�W"��
�� �.̅��h�|�9���� N����Dhd!KO Z���n���?��DN��lN��~,ȩ��J�]�����F����k��߂��uh��rT�[bI>$l.0�7OV=f��Z�r0�e`�K�m��?_a��V%�5 �tP��_��e��ul���a��I�h�����dh�e"�"G�,�[�����?H��y��	�
E��<9�R�!���e����[����8u�U��\��?��s{#R%
D������E(����h��O�"0��ЬlD�p� �+E�H�L����"�j�a��Km#�%�&D�
�����L��4T��z
��溉+�����/3��NG��IE�Vl��S�"��ʇV�sM1J7��������68w�#A"F ��01<��
Pj�fgav�7��bN�t���@@�LF�B@��g#,6\���j�Lv$Jda��K�c��$g(���C{stS�S�Cza:d��n����;}������x �Ȫ�������}�3�۱)�uj8o���31�~�֝����O�F$��d��r-60�d�L5g�<x"Rxb�|���ȤO�����w��gL��$2f%� �1�c��9����.��L��R����?T[��Wؙ�2�4΃V��#﹞�}���]xJ͎�o���S)�ӶbD���1� M�Mc ��Ъ�@����D�4Hԓ!QO�@1�(�0D�20�����HN�WB"�E%�+.	�9�u��{�`��rL��x��{���u��8ʌz�P�Y�Q��c������]7���7�7f��K�h�yG!"x��1+�� @���9 *,QZ]i��v�*�ȫq�Y�̦B���X>!�,̡�035��05*��b0-6�y�!=4꫓a�G��h�D��d�����U���),�:�R�Asz�bs�}�3��h����Z�?��{���l�yo>",�YHKAQ���3�cs@RX]E5�M(^�5+:аj��k�!IA Z D0��9Y4�LIô�XL	�Ġ(L��@J�L� ��)��'��՟(`��V�x}��z�P ���e1�N���椾���>w�|b��'��(~�E��a�0Qb:^"C:�F����	ya1t�հ7�GQ�"T,kG^�|��NditH�+� ���9T:f��1=6S�#1)83�#�Z�����2ξԽ!P�F	��[s{��e�z�va����L%�I�%���%㇖/�ܭ��u'�k^(z���/Ka>lG���:�)2T0�f�yP�A_]�&/Z���P���ks"[oY�B�H�0sitxS2����i�����X�˦Cy�sr��ǣ�5o��{Bq�{����}۔'�0�1��[(�_�X�U�{�(���uo����?�tČ89a���,.������(X�
sm=�E%�;\`L�Pi�$�#��G�	�,*f��13%3�ᗙ�̪�P͕���ǣ�c9j>�#�i�[���w�������f��GK-�͔��q~X��*w�_�Q�8�n?�P��,�HR���E�D���2�k�7�	��`�������"�,6дz�)ĉ�gs���\*~Y4��� �I�a�cá�<��T����c�}g�߉��46QY~A~��^SAv�rm�ҏ8?.~�.�@w+�g�h��[�
d=QL�g��[<J����s�<4/����*H�J�s��0����l]�ň����F0���lb��`4y�81��a�O@�k	*?����V�z'�zSm���pO�Ō��5)�K_����O���_U�|P }o0�SQ��
�N92MĲ%H��A!�`L�;\���n���V���\W����Bp��荠��oI���8��\��T�Z�B�I������Q�� e/�p>Jq�o��N�9�G����0ρ(�]�X����E���_��-_��%��p>IA��0�j�"�/G�\	�R�l�<����*��oDq�"T���|���@WUi~!�V;�4:P�R�
�	2�:���,�
�$	�+�`����(y�������w�M1�2-����z��T����)O2���N�n�Ԉ��\����8���=� YEG�P�t��4�l�¼�J�a��E޼&�-Z��+Ѱz5��/G~���+!v�gs�m��mq���G�ΆL5��S�:5��a�B��4�=̈́�A�[�3�;YG�g�1_�Ӆx����6��g�'�o�?��_IQq?�kAp�'��1T��b�#$��T��J4��X����P�A_Yk}#�[P�x)*����e��`�����Da	�+Rh\�2��Z:�QPw��������� ���!��Y#ֆ^������ʂ�?�Cm���D�-|�p�0Qq%%�>Ȼ��7|��-���)��3�	�H��"�/F��@�J��������	�+ʢʫ`�������2��Vd���iވ�ކQP]��10m'�z`���p������M�.����ryЙ���e���B�ڟQ�y��Q~�U����'
/s�z��DD}��7	3���gv BBb�@F%�t.�Yb�r�jH�&��vh�N��V���иH�MCP`0����9�yc�<:
�sc�=>�$�6������!�e￉�͹�u�
�"�s?c9g��m��[�X��/����n�(��s
\p<̈́��QHw�#�7�Թ�MA29i�dd��N���`A�B!�A)�A"�ţ ��t�\d�}�h�
Ѷ�P���Pu���C�$藓������C���XxE�'�)
O�y����}��3����2��Gɞ��FB��9�<M��ql�aH��I"����8Ɂ`���@�6��P�[� h
�x~8d�QP.� �媹P��	��ɐ���hh�FC{n4gF@�9Ĺ1�l'A�G����E�n��Esi�7�i�˝&�����(bf�9�'�S3?Wܘ���Y��$,h"�r�d���ays_���a���a��C�yM�?4w|��յiP]���	P�ͩ�:3D�0���Asv8�]á>;�S#@t�9��#�>���IЪI �@��V���5����#�FQ\\��uB���қe�o(�O�Jyu�?��H��:j���b�<[i�� hn@}���s@ܜ�{�g���$(��qy,���:;�S$�N�@���p�:G@sb$T�#At� qb��FA}l��F�PG�F@�����a�(�F�M�ŧOY�Y��鲌F��i<7wv=�˫�YN��+�>��V���H����� �"�;��@���A{���P�����T(�O���$(�&�8=���P� ��#�UGG@}�h����8hO���T�z����ɰ�`�`h"�N���_(�v�
Unnn@AA�h �BC�P��sR��f�z�l�#�^�ߚ�~i�<e��a��H�G�p*��~���ao�̈́��O��������)P����P�́���	퇳�=��� �B�ꡠ���aѓ`����H?��H��8�Ze2�&����鑝=<))i\ZZZH� K+_������|�J��+��j�� ko$����܍��n4��"��
��@�.�Cw��._��Ά��4]>Pẃ�/��|��0�K�0\��;�;Ѱ�%��8���(���5$��$�EB��fͰϕ�"βU�e<7Y*�N
�#��i愄�����Rɩђ�-�P��KI��H?��6e��F�����E��t2P�<4<�@��t�=�����*��d�=NG���?��p����l��`�t���A1��2a96�"��� �䰑�d��uUTM�GgвX,��X,Eİ���8�LA�P��E�D������:�
H�V��ޖ�3d��܋v;$���݅���Lw���_?>g��3�EϘ��'9�Gtw�#���!�]ԟ�.�Ks�ߍw;oF��W܆αnk+�] !��@D���}��Ƭe|#���q}D"�<o���>�F���4��Ȥ����7����>+�$}o�?�G]o�[s_�[[_�[K_�[s_�[��ȷ��!o���n���u���t�y��6��Ҵ����j�&�՞�V}r�[��oU�#�*O�x�<5�n��I��@O�ڵ���q8i=1_(�s�J��N7�}�@VVְ���QiԔ���,�/�Q�y�I����-Þ�����J�4�|T0��め��^Z���O���U����۔���䁒kI�W
.�軦(όP1�[7l��2��n��cq��s5|'������^����3�F���d����iTz~��5ϿE�dN�t��v��v�qj��E�Ǯk?q�h����_?����}���j�wy{�����^�Ҿ����]�7��;��}߹-�kN5�����wz�K�{���j�.�֤�䪩���̈F�����}��B���5:11�+555,!).9#3���II��Q��8J.�AQ��VOѨ��JCѨ��ZKQ�4�FG1��REQj���Pt#E,P��J�0����J!SS))���������L?*�:����_��? �0�n"    IEND�B`�                                                                                                                                                                                                                                                                                 main.c                                                                                              0000600 0000000 0000000 00000001033 11753130504 010630  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   /*
 * =====================================================================================
 *
 *       Filename:  main.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Friday 11 May 2012 11:53:53  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
	printf("\nEnter \n");
	return 0;
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     output.txt                                                                                          0000600 0000000 0000000 00000314567 11745756426 011706  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   MyListener init
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
32
goal: 
[770, 570]
757.4567384147547
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
38
goal: 
[770, 570]
739.8274381571126
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
32
goal: 
[770, 570]
757.4567384147547
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
32
goal: 
[770, 570]
757.4567384147547
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
32
goal: 
[770, 570]
757.4567384147547
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
32
goal: 
[770, 570]
757.4567384147547
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
26
goal: 
[770, 570]
779.3181525569692
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
8
goal: 
[770, 570]
866.790055319049
p: 
5
20
goal: 
[770, 570]
805.0669880542763
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
5
14
goal: 
[770, 570]
834.3434110843378
p: 
8
32
goal: 
[770, 570]
730.106206640712
p: 
5
32
goal: 
[770, 570]
757.4567384147547
p: 
2
32
goal: 
[770, 570]
779.4652692106816
p: 
5
44
goal: 
[770, 570]
726.7383063699077
p: 
13
31
goal: 
[770, 570]
680.1038738962449
p: 
3
36
goal: 
[770, 570]
765.4540037557281
p: 
17
35
goal: 
[770, 570]
626.9154991845718
p: 
19
33
goal: 
[770, 570]
620.316451401971
p: 
19
30
goal: 
[770, 570]
631.4416734297104
p: 
8
30
goal: 
[770, 570]
739.9255676015235
p: 
23
37
goal: 
[770, 570]
566.9843741147305
p: 
25
35
goal: 
[770, 570]
560.5745002316683
p: 
25
32
goal: 
[770, 570]
571.9849654843093
p: 
13
31
goal: 
[770, 570]
680.1038738962449
p: 
29
39
goal: 
[770, 570]
507.0696172374384
p: 
31
37
goal: 
[770, 570]
500.8942908227561
p: 
30
34
goal: 
[770, 570]
512.6548900435718
p: 
19
33
goal: 
[770, 570]
620.316451401971
p: 
35
41
goal: 
[770, 570]
447.17768194339465
p: 
36
38
goal: 
[770, 570]
441.30087319931175
p: 
36
36
goal: 
[770, 570]
453.50121638217774
p: 
25
35
goal: 
[770, 570]
560.5745002316683
p: 
40
42
goal: 
[770, 570]
387.31933803729794
p: 
42
40
goal: 
[770, 570]
381.83488661058016
p: 
42
37
goal: 
[770, 570]
394.6032438709028
p: 
31
37
goal: 
[770, 570]
500.8942908227561
p: 
46
44
goal: 
[770, 570]
327.51291554048635
p: 
48
42
goal: 
[770, 570]
322.56681543232315
p: 
48
39
goal: 
[770, 570]
336.0954280045473
p: 
36
38
goal: 
[770, 570]
441.30087319931175
p: 
52
46
goal: 
[770, 570]
267.7932036344558
p: 
53
44
goal: 
[770, 570]
263.6305501607147
p: 
53
41
goal: 
[770, 570]
278.2239656133895
p: 
42
40
goal: 
[770, 570]
381.83488661058016
p: 
58
48
goal: 
[770, 570]
208.23520622812413
p: 
59
45
goal: 
[770, 570]
205.31172500072887
p: 
59
43
goal: 
[770, 570]
221.4888009271644
p: 
48
42
goal: 
[770, 570]
322.56681543232315
p: 
63
49
goal: 
[770, 570]
149.03248794997228
p: 
65
47
goal: 
[770, 570]
148.3394137586222
p: 
65
44
goal: 
[770, 570]
167.0509254277545
p: 
53
44
goal: 
[770, 570]
263.6305501607147
p: 
69
51
goal: 
[770, 570]
90.88071095117405
p: 
71
49
goal: 
[770, 570]
95.16353677996351
p: 
71
46
goal: 
[770, 570]
118.12948083830852
p: 
59
45
goal: 
[770, 570]
205.31172500072887
p: 
75
53
goal: 
[770, 570]
38.829889378861964
p: 
76
51
goal: 
[770, 570]
57.510482500446756
p: 
76
48
goal: 
[770, 570]
84.87035175330884
p: 
65
47
goal: 
[770, 570]
148.3394137586222
DONE
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
34
goal: 
[770, 570]
751.0938821445523
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
40
goal: 
[770, 570]
734.9462208081634
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
34
goal: 
[770, 570]
751.0938821445523
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
34
goal: 
[770, 570]
751.0938821445523
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
34
goal: 
[770, 570]
751.0938821445523
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
34
goal: 
[770, 570]
751.0938821445523
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
34
goal: 
[770, 570]
751.0938821445523
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
28
goal: 
[770, 570]
771.5815524783071
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
22
goal: 
[770, 570]
796.0742204529564
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
4
goal: 
[770, 570]
890.0125738410383
p: 
5
16
goal: 
[770, 570]
824.2149215039833
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
5
10
goal: 
[770, 570]
855.6437980871127
p: 
8
34
goal: 
[770, 570]
723.7338749191333
p: 
5
34
goal: 
[770, 570]
751.0938821445523
p: 
2
34
goal: 
[770, 570]
773.4996775462099
p: 
5
46
goal: 
[770, 570]
723.429246837945
p: 
13
33
goal: 
[770, 570]
672.969159860635
p: 
3
38
goal: 
[770, 570]
760.3168446197124
p: 
17
37
goal: 
[770, 570]
620.4611639707443
p: 
19
35
goal: 
[770, 570]
613.0608439410398
p: 
19
32
goal: 
[770, 570]
623.4383368732136
p: 
8
32
goal: 
[770, 570]
732.8923309504752
p: 
23
39
goal: 
[770, 570]
560.468715475966
p: 
25
37
goal: 
[770, 570]
553.1724473097581
p: 
25
34
goal: 
[770, 570]
563.7627704438529
p: 
13
33
goal: 
[770, 570]
672.969159860635
p: 
29
41
goal: 
[770, 570]
500.47815628786554
p: 
31
39
goal: 
[770, 570]
493.3112246750834
p: 
30
36
goal: 
[770, 570]
504.16424361797925
p: 
19
35
goal: 
[770, 570]
613.0608439410398
p: 
35
43
goal: 
[770, 570]
440.49013051719027
p: 
36
40
goal: 
[770, 570]
433.48843370612593
p: 
36
38
goal: 
[770, 570]
444.6738008656837
p: 
25
37
goal: 
[770, 570]
553.1724473097581
p: 
40
44
goal: 
[770, 570]
380.50602246396915
p: 
42
42
goal: 
[770, 570]
373.7225304451771
p: 
42
39
goal: 
[770, 570]
385.3414637027457
p: 
31
39
goal: 
[770, 570]
493.3112246750834
p: 
46
46
goal: 
[770, 570]
320.52794108852055
p: 
48
44
goal: 
[770, 570]
314.04599536771445
p: 
48
41
goal: 
[770, 570]
326.2535026012925
p: 
36
40
goal: 
[770, 570]
433.48843370612593
p: 
52
48
goal: 
[770, 570]
260.5601059018694
p: 
53
46
goal: 
[770, 570]
254.52208435828888
p: 
53
43
goal: 
[770, 570]
267.5717581501389
p: 
42
42
goal: 
[770, 570]
373.7225304451771
p: 
58
50
goal: 
[770, 570]
200.61188300821277
p: 
59
47
goal: 
[770, 570]
195.29008303396907
p: 
59
45
goal: 
[770, 570]
209.63849041343138
p: 
48
44
goal: 
[770, 570]
314.04599536771445
p: 
63
51
goal: 
[770, 570]
140.70819669224284
p: 
65
49
goal: 
[770, 570]
136.72886104800307
p: 
65
46
goal: 
[770, 570]
153.30329439551758
p: 
53
46
goal: 
[770, 570]
254.52208435828888
p: 
69
53
goal: 
[770, 570]
80.94631205563294
p: 
71
51
goal: 
[770, 570]
80.3193601859648
p: 
71
48
goal: 
[770, 570]
101.2686688416416
p: 
59
47
goal: 
[770, 570]
195.29008303396907
p: 
75
55
goal: 
[770, 570]
22.48679387481583
p: 
76
53
goal: 
[770, 570]
37.516776382657
p: 
76
50
goal: 
[770, 570]
64.87392628892115
p: 
65
49
goal: 
[770, 570]
136.72886104800307
DONE
p: 
17
35
goal: 
[770, 570]
633.0283485642636
p: 
21
39
goal: 
[770, 570]
580.466020090053
p: 
23
36
goal: 
[770, 570]
573.1326474403932
p: 
23
34
goal: 
[770, 570]
583.6472296251574
p: 
11
33
goal: 
[770, 570]
692.9420962653826
p: 
27
40
goal: 
[770, 570]
520.474772613553
p: 
29
38
goal: 
[770, 570]
513.2613592282838
p: 
29
35
goal: 
[770, 570]
524.0202508780316
p: 
17
35
goal: 
[770, 570]
633.0283485642636
p: 
23
36
goal: 
[770, 570]
573.1326474403932
p: 
26
46
goal: 
[770, 570]
512.8595480915632
p: 
25
35
goal: 
[770, 570]
559.0341909647668
p: 
23
51
goal: 
[770, 570]
538.5854421570704
p: 
26
52
goal: 
[770, 570]
511.7099082150331
p: 
31
30
goal: 
[770, 570]
524.2450404011142
p: 
24
39
goal: 
[770, 570]
556.2039182606615
p: 
28
57
goal: 
[770, 570]
489.7097536448853
p: 
30
56
goal: 
[770, 570]
467.87139254509805
p: 
24
46
goal: 
[770, 570]
539.5168219021291
p: 
34
60
goal: 
[770, 570]
427.37728229058627
p: 
35
58
goal: 
[770, 570]
410.5977706171364
p: 
35
55
goal: 
[770, 570]
411.14726277291527
p: 
24
54
goal: 
[770, 570]
525.7534935546139
p: 
40
62
goal: 
[770, 570]
372.2031355308377
p: 
41
59
goal: 
[770, 570]
354.22789811913646
p: 
41
57
goal: 
[770, 570]
353.4486836681188
p: 
30
56
goal: 
[770, 570]
467.87139254509805
p: 
45
63
goal: 
[770, 570]
318.777339339471
p: 
47
61
goal: 
[770, 570]
299.2728916432384
p: 
47
58
goal: 
[770, 570]
296.66455397343424
p: 
35
58
goal: 
[770, 570]
410.5977706171364
p: 
51
65
goal: 
[770, 570]
268.14690812806765
p: 
53
63
goal: 
[770, 570]
246.6804996286979
p: 
53
60
goal: 
[770, 570]
241.44088165638516
p: 
41
59
goal: 
[770, 570]
354.22789811913646
p: 
57
67
goal: 
[770, 570]
222.23124888982647
p: 
58
65
goal: 
[770, 570]
198.3390843127731
p: 
58
62
goal: 
[770, 570]
189.1499283092812
p: 
47
61
goal: 
[770, 570]
299.27292180232877
p: 
64
61
goal: 
[770, 570]
131.89097832430863
p: 
63
58
goal: 
[770, 570]
134.33882632980468
p: 
61
57
goal: 
[770, 570]
155.34693661480415
p: 
54
65
goal: 
[770, 570]
246.39093026150084
p: 
69
57
goal: 
[770, 570]
76.55985908045595
p: 
68
55
goal: 
[770, 570]
86.69581971420195
p: 
66
53
goal: 
[770, 570]
112.24492952353035
p: 
58
62
goal: 
[770, 570]
189.1499283092812
p: 
73
61
goal: 
[770, 570]
59.31002558283985
p: 
75
59
goal: 
[770, 570]
31.95263227546885
p: 
75
56
goal: 
[770, 570]
19.157559520042682
p: 
63
56
goal: 
[770, 570]
133.79696782782253
DONE
p: 
27
40
goal: 
[770, 570]
520.474772613553
p: 
26
46
goal: 
[770, 570]
512.8595480915632
p: 
25
35
goal: 
[770, 570]
559.0341909647668
p: 
23
51
goal: 
[770, 570]
538.5854421570704
p: 
26
52
goal: 
[770, 570]
511.7099082150331
p: 
30
56
goal: 
[770, 570]
467.87139254509805
p: 
24
46
goal: 
[770, 570]
539.5168219021291
p: 
35
55
goal: 
[770, 570]
411.14726277291527
p: 
24
54
goal: 
[770, 570]
525.7534935546139
p: 
41
54
goal: 
[770, 570]
354.7838845704189
p: 
40
51
goal: 
[770, 570]
366.3284219513894
p: 
38
50
goal: 
[770, 570]
390.7985251419686
p: 
47
56
goal: 
[770, 570]
296.567894552552
p: 
47
53
goal: 
[770, 570]
298.9853494031711
p: 
35
52
goal: 
[770, 570]
413.51019179566117
p: 
51
60
goal: 
[770, 570]
256.61203597203036
p: 
53
57
goal: 
[770, 570]
239.23533191027676
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
41
54
goal: 
[770, 570]
354.7838845704189
p: 
57
61
goal: 
[770, 570]
203.2921481558213
p: 
58
59
goal: 
[770, 570]
183.61570521423332
p: 
58
56
goal: 
[770, 570]
182.06635621070646
p: 
47
56
goal: 
[770, 570]
296.567894552552
p: 
62
63
goal: 
[770, 570]
154.93787206780723
p: 
64
61
goal: 
[770, 570]
131.89270500233266
p: 
64
58
goal: 
[770, 570]
125.80242986370236
p: 
53
57
goal: 
[770, 570]
239.23533191027676
p: 
68
65
goal: 
[770, 570]
117.82854562627918
p: 
70
63
goal: 
[770, 570]
90.97482799520222
p: 
70
60
goal: 
[770, 570]
75.52562425953073
p: 
58
59
goal: 
[770, 570]
183.61570521423332
p: 
75
59
goal: 
[770, 570]
26.526637712799946
p: 
75
56
goal: 
[770, 570]
19.1593850014604
p: 
72
55
goal: 
[770, 570]
44.85059555289997
p: 
65
63
goal: 
[770, 570]
135.05990456806276
DONE
p: 
30
56
goal: 
[770, 570]
467.87139254509805
p: 
35
55
goal: 
[770, 570]
411.14726277291527
p: 
24
54
goal: 
[770, 570]
525.7534935546139
p: 
41
54
goal: 
[770, 570]
354.7838845704189
p: 
40
51
goal: 
[770, 570]
366.3284219513894
p: 
38
50
goal: 
[770, 570]
390.7985251419686
p: 
47
56
goal: 
[770, 570]
296.567894552552
p: 
47
53
goal: 
[770, 570]
298.9853494031711
p: 
35
52
goal: 
[770, 570]
413.51019179566117
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
41
54
goal: 
[770, 570]
354.7838845704189
p: 
58
54
goal: 
[770, 570]
184.60464482515155
p: 
57
51
goal: 
[770, 570]
198.73900123525908
p: 
55
49
goal: 
[770, 570]
224.6609491530426
p: 
62
58
goal: 
[770, 570]
141.16900546868263
p: 
64
55
goal: 
[770, 570]
125.51507097125193
p: 
64
53
goal: 
[770, 570]
131.06763824698126
p: 
53
52
goal: 
[770, 570]
244.1382641159195
p: 
68
59
goal: 
[770, 570]
88.32162694893498
p: 
70
57
goal: 
[770, 570]
68.03650825276549
p: 
70
54
goal: 
[770, 570]
71.0689388847726
p: 
58
54
goal: 
[770, 570]
184.60464482515155
p: 
74
61
goal: 
[770, 570]
53.595771598223074
p: 
75
59
goal: 
[770, 570]
26.526875691475773
p: 
75
56
goal: 
[770, 570]
11.074186976284619
p: 
64
55
goal: 
[770, 570]
125.51507097125193
DONE
p: 
47
56
goal: 
[770, 570]
296.567894552552
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
41
54
goal: 
[770, 570]
354.7838845704189
p: 
58
54
goal: 
[770, 570]
184.60464482515155
p: 
57
51
goal: 
[770, 570]
198.73900123525908
p: 
55
49
goal: 
[770, 570]
224.6609491530426
p: 
53
52
goal: 
[770, 570]
244.1382641159195
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
58
50
goal: 
[770, 570]
197.30283778506833
p: 
55
49
goal: 
[770, 570]
224.6609587094739
p: 
53
50
goal: 
[770, 570]
247.31136603726168
p: 
53
54
goal: 
[770, 570]
237.03624421760156
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
58
54
goal: 
[770, 570]
184.60464482515155
p: 
57
51
goal: 
[770, 570]
198.73900123525908
p: 
55
49
goal: 
[770, 570]
224.6609491530426
p: 
53
52
goal: 
[770, 570]
244.1382641159195
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
57
56
goal: 
[770, 570]
198.1325062617451
p: 
58
54
goal: 
[770, 570]
184.60464482515155
p: 
58
51
goal: 
[770, 570]
191.06656636232228
p: 
47
50
goal: 
[770, 570]
303.85572903934866
p: 
53
52
goal: 
[770, 570]
244.1382641159195
p: 
53
54
goal: 
[770, 570]
231.87085948101247
p: 
55
50
goal: 
[770, 570]
226.76031664421154
p: 
47
49
goal: 
[770, 570]
304.9861031709407
p: 
57
54
goal: 
[770, 570]
192.96702550376187
p: 
41
48
goal: 
[770, 570]
362.71372111273706
p: 
41
51
goal: 
[770, 570]
357.899874484659
p: 
43
53
goal: 
[770, 570]
339.6240369073888
p: 
53
48
goal: 
[770, 570]
255.2272221199033
p: 
47
56
goal: 
[770, 570]
296.567894552552
p: 
47
53
goal: 
[770, 570]
298.9853494031711
p: 
35
52
goal: 
[770, 570]
413.51019179566117
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
41
54
goal: 
[770, 570]
354.7838845704189
p: 
58
54
goal: 
[770, 570]
184.60464482515155
p: 
57
51
goal: 
[770, 570]
198.73900123525908
p: 
55
49
goal: 
[770, 570]
224.6609491530426
p: 
53
52
goal: 
[770, 570]
244.1382641159195
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
53
52
goal: 
[770, 570]
244.1392830734681
p: 
52
49
goal: 
[770, 570]
258.7286909910106
p: 
49
48
goal: 
[770, 570]
284.65108875574373
p: 
42
56
goal: 
[770, 570]
345.02740480020196
p: 
57
56
goal: 
[770, 570]
198.133482376915
p: 
58
54
goal: 
[770, 570]
184.60567003182564
p: 
58
51
goal: 
[770, 570]
191.0675587230579
p: 
47
50
goal: 
[770, 570]
303.85674358597026
p: 
53
52
goal: 
[770, 570]
244.1392830734681
p: 
53
54
goal: 
[770, 570]
231.87189315436927
p: 
55
50
goal: 
[770, 570]
226.7612552600814
p: 
57
48
goal: 
[770, 570]
208.2047225855965
p: 
47
53
goal: 
[770, 570]
298.9853494031711
p: 
62
52
goal: 
[770, 570]
155.46812504019755
p: 
49
54
goal: 
[770, 570]
272.1593034395032
p: 
45
48
goal: 
[770, 570]
330.2446597825461
p: 
35
50
goal: 
[770, 570]
415.73316812015366
p: 
35
53
goal: 
[770, 570]
412.7567798858745
p: 
37
55
goal: 
[770, 570]
395.7490402551265
p: 
47
49
goal: 
[770, 570]
304.9861031709407
p: 
46
52
goal: 
[770, 570]
308.61016681455493
p: 
39
49
goal: 
[770, 570]
382.17221205801553
p: 
30
52
goal: 
[770, 570]
470.43269219684277
p: 
30
55
goal: 
[770, 570]
468.8754053714191
p: 
41
51
goal: 
[770, 570]
357.899874484659
p: 
30
49
goal: 
[770, 570]
473.5683017455188
p: 
40
54
goal: 
[770, 570]
363.6403639874827
p: 
24
54
goal: 
[770, 570]
526.2888063524238
p: 
24
56
goal: 
[770, 570]
525.8518489876561
p: 
35
53
goal: 
[770, 570]
412.7567798858745
p: 
27
47
goal: 
[770, 570]
503.8036121185505
p: 
25
48
goal: 
[770, 570]
522.8626736782492
p: 
24
51
goal: 
[770, 570]
528.1446651107995
p: 
35
55
goal: 
[770, 570]
420.03389436409276
p: 
24
48
goal: 
[770, 570]
531.4046643136595
p: 
24
51
goal: 
[770, 570]
528.1446798019249
p: 
26
53
goal: 
[770, 570]
510.6314763708504
p: 
27
41
goal: 
[770, 570]
518.8065997432988
p: 
24
42
goal: 
[770, 570]
541.3135592973259
p: 
27
53
goal: 
[770, 570]
495.6570120122887
p: 
30
55
goal: 
[770, 570]
468.8754053714191
p: 
30
52
goal: 
[770, 570]
470.43269219684277
p: 
30
36
goal: 
[770, 570]
512.8927499878538
p: 
27
35
goal: 
[770, 570]
540.0948956487141
p: 
24
36
goal: 
[770, 570]
560.8561010503241
p: 
27
47
goal: 
[770, 570]
503.8036121185505
p: 
32
30
goal: 
[770, 570]
513.467397315524
p: 
25
39
goal: 
[770, 570]
544.8875007592205
p: 
30
49
goal: 
[770, 570]
473.5682245135111
p: 
30
49
goal: 
[770, 570]
473.56829700322476
p: 
32
24
goal: 
[770, 570]
546.4292697122469
p: 
30
25
goal: 
[770, 570]
563.0280445180705
p: 
32
36
goal: 
[770, 570]
485.70833782094405
p: 
29
52
goal: 
[770, 570]
478.9542403620736
p: 
30
30
goal: 
[770, 570]
540.1834563558381
p: 
27
29
goal: 
[770, 570]
566.9609375340375
p: 
24
30
goal: 
[770, 570]
585.9170271520454
p: 
27
41
goal: 
[770, 570]
518.8065997432988
p: 
22
36
goal: 
[770, 570]
582.1629864263955
p: 
20
38
goal: 
[770, 570]
597.9070155813675
p: 
19
41
goal: 
[770, 570]
598.8345488148099
p: 
32
24
goal: 
[770, 570]
546.4292517760291
p: 
25
33
goal: 
[770, 570]
566.8887996477881
p: 
32
30
goal: 
[770, 570]
513.467381793955
p: 
32
30
goal: 
[770, 570]
513.467397315524
p: 
30
24
goal: 
[770, 570]
572.4835020033885
p: 
27
23
goal: 
[770, 570]
598.6542517081472
p: 
24
24
goal: 
[770, 570]
615.8229935160731
p: 
27
35
goal: 
[770, 570]
540.0948956487141
p: 
22
30
goal: 
[770, 570]
605.5162488521892
p: 
20
32
goal: 
[770, 570]
619.120897640188
p: 
19
35
goal: 
[770, 570]
617.503301186551
p: 
29
39
goal: 
[770, 570]
502.99947598944834
p: 
25
27
goal: 
[770, 570]
594.1576460103994
p: 
25
22
goal: 
[770, 570]
622.9673126201377
p: 
24
24
goal: 
[770, 570]
616.2961925945627
p: 
22
24
goal: 
[770, 570]
633.7082466729528
p: 
20
26
goal: 
[770, 570]
645.235284623566
p: 
19
29
goal: 
[770, 570]
641.2626896315013
p: 
29
33
goal: 
[770, 570]
526.7532434259444
p: 
24
31
goal: 
[770, 570]
578.4185506756148
p: 
22
30
goal: 
[770, 570]
605.5162488521892
p: 
19
31
goal: 
[770, 570]
625.6981937043336
p: 
22
42
goal: 
[770, 570]
564.2495528760835
p: 
27
29
goal: 
[770, 570]
566.9609375340375
p: 
30
30
goal: 
[770, 570]
532.4562956222243
p: 
29
28
goal: 
[770, 570]
553.1567591174371
p: 
27
26
goal: 
[770, 570]
580.442397371286
p: 
20
35
goal: 
[770, 570]
608.5671628422162
p: 
24
28
goal: 
[770, 570]
591.1851398097571
p: 
24
31
goal: 
[770, 570]
578.4185506756148
p: 
17
33
goal: 
[770, 570]
639.9868399834471
p: 
15
34
goal: 
[770, 570]
655.1070456415424
p: 
14
37
goal: 
[770, 570]
655.1887143583667
p: 
24
42
goal: 
[770, 570]
541.3135592973259
p: 
13
40
goal: 
[770, 570]
656.4117464534745
p: 
13
42
goal: 
[770, 570]
650.2376424542192
p: 
15
45
goal: 
[770, 570]
630.354756522152
p: 
25
39
goal: 
[770, 570]
549.1781311501051
p: 
24
21
goal: 
[770, 570]
630.4367566398764
p: 
27
32
goal: 
[770, 570]
551.3467343679742
p: 
24
25
goal: 
[770, 570]
607.0429884173362
p: 
22
24
goal: 
[770, 570]
633.7082234737376
p: 
19
25
goal: 
[770, 570]
652.2510273789436
p: 
22
36
goal: 
[770, 570]
582.1629864263955
p: 
24
25
goal: 
[770, 570]
607.0429884173362
p: 
22
24
goal: 
[770, 570]
633.7082234737376
p: 
19
25
goal: 
[770, 570]
652.2510273789436
p: 
22
36
goal: 
[770, 570]
582.1629864263955
p: 
22
18
goal: 
[770, 570]
666.1248449199436
p: 
20
20
goal: 
[770, 570]
675.682217589603
p: 
19
23
goal: 
[770, 570]
669.5710173429354
p: 
29
27
goal: 
[770, 570]
555.9941421354478
p: 
17
27
goal: 
[770, 570]
664.5284269452044
p: 
15
28
goal: 
[770, 570]
677.6885847273121
p: 
14
31
goal: 
[770, 570]
675.4690603956361
p: 
24
36
goal: 
[770, 570]
560.8561010503241
p: 
30
24
goal: 
[770, 570]
564.4565443456964
p: 
20
29
goal: 
[770, 570]
632.462244612667
p: 
24
22
goal: 
[770, 570]
621.8646997470436
p: 
30
24
goal: 
[770, 570]
564.4565443456964
p: 
20
29
goal: 
[770, 570]
632.462244612667
p: 
24
22
goal: 
[770, 570]
621.8646997470436
p: 
13
34
goal: 
[770, 570]
674.3531749165058
p: 
13
36
goal: 
[770, 570]
665.8842751414678
p: 
15
39
goal: 
[770, 570]
644.3960222909236
p: 
25
33
goal: 
[770, 570]
571.3306956232685
p: 
22
16
goal: 
[770, 570]
674.0387146800459
p: 
20
18
goal: 
[770, 570]
682.9172559234133
p: 
19
21
goal: 
[770, 570]
676.0959228722944
p: 
30
25
goal: 
[770, 570]
563.0280445180705
p: 
17
26
goal: 
[770, 570]
671.3969243294447
p: 
14
28
goal: 
[770, 570]
684.3717008883295
p: 
14
30
goal: 
[770, 570]
681.9334731145997
p: 
24
35
goal: 
[770, 570]
567.3022531230071
p: 
24
19
goal: 
[770, 570]
640.0268430485623
p: 
22
18
goal: 
[770, 570]
666.1248361887899
p: 
19
19
goal: 
[770, 570]
683.0553241458532
p: 
22
30
goal: 
[770, 570]
605.5162488521892
p: 
24
19
goal: 
[770, 570]
640.0268430485623
p: 
22
18
goal: 
[770, 570]
666.1248361887899
p: 
19
19
goal: 
[770, 570]
683.0553241458532
p: 
22
30
goal: 
[770, 570]
605.5162488521892
p: 
24
19
goal: 
[770, 570]
640.0268608243176
p: 
22
18
goal: 
[770, 570]
666.1248623822516
p: 
19
19
goal: 
[770, 570]
683.0553574580434
p: 
22
30
goal: 
[770, 570]
605.5162751767275
p: 
18
23
goal: 
[770, 570]
670.3226965167107
p: 
18
26
goal: 
[770, 570]
657.4919894564681
p: 
20
28
goal: 
[770, 570]
633.3506327792123
p: 
17
21
goal: 
[770, 570]
693.4067778336986
p: 
15
22
goal: 
[770, 570]
704.6689964127214
p: 
14
25
goal: 
[770, 570]
700.317536333373
p: 
24
30
goal: 
[770, 570]
585.9170271520454
p: 
13
50
goal: 
[770, 570]
641.9557673721371
p: 
15
50
goal: 
[770, 570]
614.6657400760107
p: 
17
39
goal: 
[770, 570]
624.3292016877002
p: 
16
56
goal: 
[770, 570]
604.1290012751683
p: 
55
49
goal: 
[770, 570]
230.7841750590744
p: 
53
50
goal: 
[770, 570]
247.3113583873292
p: 
52
53
goal: 
[770, 570]
250.78465849818733
p: 
20
28
goal: 
[770, 570]
637.4995854874331
p: 
17
27
goal: 
[770, 570]
664.5284269452044
p: 
14
28
goal: 
[770, 570]
684.3716870512048
p: 
17
39
goal: 
[770, 570]
620.2969293014565
p: 
13
28
goal: 
[770, 570]
697.0136372655293
p: 
13
30
goal: 
[770, 570]
686.4362636924294
p: 
15
33
goal: 
[770, 570]
663.5852228867932
p: 
25
27
goal: 
[770, 570]
598.6993467545302
p: 
9
33
goal: 
[770, 570]
712.1388266605404
p: 
20
38
goal: 
[770, 570]
597.9070155813675
p: 
25
27
goal: 
[770, 570]
592.063350796343
p: 
24
24
goal: 
[770, 570]
612.9479004654312
p: 
22
22
goal: 
[770, 570]
640.2495051471956
p: 
15
31
goal: 
[770, 570]
666.5631111443294
p: 
30
31
goal: 
[770, 570]
536.0197311384238
p: 
31
28
goal: 
[770, 570]
533.8134889823411
p: 
31
26
goal: 
[770, 570]
548.9657003126724
p: 
20
25
goal: 
[770, 570]
650.6313802606566
p: 
25
27
goal: 
[770, 570]
592.063350796343
p: 
29
36
goal: 
[770, 570]
517.7284558359863
p: 
32
36
goal: 
[770, 570]
492.94303227760696
p: 
28
25
goal: 
[770, 570]
582.1008637609626
p: 
31
42
goal: 
[770, 570]
479.4949891422897
p: 
30
31
goal: 
[770, 570]
536.0197311384238
p: 
24
39
goal: 
[770, 570]
555.2986263051544
p: 
25
41
goal: 
[770, 570]
532.7896451118836
p: 
28
42
goal: 
[770, 570]
505.43004852508744
p: 
32
31
goal: 
[770, 570]
509.3335017527707
p: 
26
37
goal: 
[770, 570]
542.7613493882569
p: 
25
47
goal: 
[770, 570]
526.7623308990517
p: 
29
36
goal: 
[770, 570]
517.7284558359863
p: 
24
53
goal: 
[770, 570]
527.0516285526195
p: 
27
53
goal: 
[770, 570]
499.8267448837046
p: 
29
51
goal: 
[770, 570]
479.65476161119824
p: 
23
41
goal: 
[770, 570]
558.8651349971341
p: 
33
55
goal: 
[770, 570]
435.14356155008886
p: 
35
53
goal: 
[770, 570]
420.8357554592968
p: 
35
50
goal: 
[770, 570]
424.39006867227914
p: 
23
49
goal: 
[770, 570]
538.7343807423359
p: 
40
55
goal: 
[770, 570]
362.4041405753585
p: 
40
52
goal: 
[770, 570]
365.1547423639145
p: 
29
51
goal: 
[770, 570]
479.65476161119824
p: 
46
56
goal: 
[770, 570]
304.5829516499516
p: 
46
54
goal: 
[770, 570]
306.2172803420159
p: 
35
53
goal: 
[770, 570]
420.8357554592968
p: 
40
55
goal: 
[770, 570]
362.4041405753585
p: 
52
53
goal: 
[770, 570]
250.78350905659104
p: 
51
50
goal: 
[770, 570]
264.4772807881511
p: 
49
49
goal: 
[770, 570]
290.0597248541102
p: 
57
54
goal: 
[770, 570]
191.6266005980359
p: 
57
52
goal: 
[770, 570]
196.74049494450463
p: 
46
51
goal: 
[770, 570]
310.26476406566184
p: 
52
53
goal: 
[770, 570]
250.78350905659104
p: 
62
48
goal: 
[770, 570]
165.1661382463377
p: 
53
55
goal: 
[770, 570]
239.4445648997239
p: 
57
52
goal: 
[770, 570]
196.74049494450463
p: 
57
49
goal: 
[770, 570]
212.76401765071006
p: 
46
54
goal: 
[770, 570]
306.2172803420159
p: 
61
53
goal: 
[770, 570]
161.4449678744656
p: 
62
51
goal: 
[770, 570]
152.890305478055
p: 
62
48
goal: 
[770, 570]
165.1663844657902
p: 
57
49
goal: 
[770, 570]
212.7640282007394
p: 
57
52
goal: 
[770, 570]
196.74061316186828
p: 
49
55
goal: 
[770, 570]
279.57006359296633
p: 
46
51
goal: 
[770, 570]
310.26494421535347
p: 
45
48
goal: 
[770, 570]
324.4047038485055
p: 
35
55
goal: 
[770, 570]
410.654940869005
p: 
50
55
goal: 
[770, 570]
263.9982556948795
p: 
52
53
goal: 
[770, 570]
250.78369005909417
p: 
52
50
goal: 
[770, 570]
256.67446835587265
p: 
40
49
goal: 
[770, 570]
369.9140292653391
p: 
57
54
goal: 
[770, 570]
191.62678267570013
p: 
57
52
goal: 
[770, 570]
196.740672602464
p: 
46
51
goal: 
[770, 570]
310.26494421535347
p: 
52
53
goal: 
[770, 570]
250.78369005909417
p: 
62
48
goal: 
[770, 570]
165.1662963678273
p: 
53
55
goal: 
[770, 570]
239.444747775941
p: 
57
52
goal: 
[770, 570]
196.740672602464
p: 
57
49
goal: 
[770, 570]
205.40281956353326
p: 
47
54
goal: 
[770, 570]
297.972119588014
p: 
62
53
goal: 
[770, 570]
153.53714310162766
p: 
48
49
goal: 
[770, 570]
292.4681744145681
p: 
40
52
goal: 
[770, 570]
365.1547423639145
p: 
40
49
goal: 
[770, 570]
369.9138602969119
p: 
30
54
goal: 
[770, 570]
468.70581279434094
p: 
44
53
goal: 
[770, 570]
322.5989288964181
p: 
46
51
goal: 
[770, 570]
310.2647913020902
p: 
46
48
goal: 
[770, 570]
316.63338880156596
p: 
50
55
goal: 
[770, 570]
263.99820568531607
p: 
52
53
goal: 
[770, 570]
250.78356092734836
p: 
52
50
goal: 
[770, 570]
256.67425111310575
p: 
40
49
goal: 
[770, 570]
369.9138602969119
p: 
57
54
goal: 
[770, 570]
191.6266922674326
p: 
57
52
goal: 
[770, 570]
196.7404657250095
p: 
46
51
goal: 
[770, 570]
310.2647913020902
p: 
52
53
goal: 
[770, 570]
250.78356092734836
p: 
62
48
goal: 
[770, 570]
165.16586548678816
p: 
53
55
goal: 
[770, 570]
239.4447050317546
p: 
57
52
goal: 
[770, 570]
196.7404657250095
p: 
57
49
goal: 
[770, 570]
205.40250760222918
p: 
47
54
goal: 
[770, 570]
297.97203469914535
p: 
62
53
goal: 
[770, 570]
153.53694877389736
p: 
48
49
goal: 
[770, 570]
292.467963903312
p: 
41
52
goal: 
[770, 570]
356.9888720262011
p: 
42
48
goal: 
[770, 570]
352.40776186200844
p: 
31
49
goal: 
[770, 570]
460.22579024955104
p: 
25
47
goal: 
[770, 570]
526.7623254675968
p: 
26
29
goal: 
[770, 570]
571.7250761305163
p: 
27
48
goal: 
[770, 570]
499.5670918944992
p: 
18
37
goal: 
[770, 570]
612.8173096663437
p: 
18
39
goal: 
[770, 570]
611.8888586415121
p: 
19
42
goal: 
[770, 570]
596.1220649344363
p: 
30
39
goal: 
[770, 570]
499.50529804121174
p: 
30
23
goal: 
[770, 570]
570.9950437160629
p: 
20
28
goal: 
[770, 570]
637.4995854874331
p: 
19
41
goal: 
[770, 570]
598.8345488148099
p: 
27
14
goal: 
[770, 570]
651.4396933671469
p: 
20
23
goal: 
[770, 570]
660.9558845938947
p: 
27
14
goal: 
[770, 570]
651.4396933671469
p: 
20
23
goal: 
[770, 570]
660.9558845938947
p: 
27
14
goal: 
[770, 570]
651.4397132506427
p: 
20
23
goal: 
[770, 570]
660.9559001605792
p: 
58
50
goal: 
[770, 570]
197.30283778506833
p: 
55
49
goal: 
[770, 570]
224.6609587094739
p: 
53
50
goal: 
[770, 570]
247.31136603726168
p: 
53
54
goal: 
[770, 570]
237.03624421760156
p: 
58
50
goal: 
[770, 570]
197.30283778506833
p: 
55
49
goal: 
[770, 570]
224.6609587094739
p: 
53
50
goal: 
[770, 570]
247.31136603726168
p: 
53
54
goal: 
[770, 570]
237.03624421760156
p: 
58
50
goal: 
[770, 570]
197.30283778506833
p: 
55
49
goal: 
[770, 570]
224.6609587094739
p: 
53
50
goal: 
[770, 570]
247.31136603726168
p: 
53
54
goal: 
[770, 570]
237.03624421760156
p: 
15
45
goal: 
[770, 570]
630.354756522152
p: 
13
44
goal: 
[770, 570]
650.5492713393085
p: 
15
44
goal: 
[770, 570]
623.5622456258719
p: 
17
33
goal: 
[770, 570]
643.7996845687106
p: 
16
50
goal: 
[770, 570]
607.5397431080456
p: 
12
39
goal: 
[770, 570]
667.6298394818576
p: 
14
56
goal: 
[770, 570]
624.0725076007941
p: 
17
56
goal: 
[770, 570]
596.7162039869553
p: 
13
51
goal: 
[770, 570]
632.910736716354
p: 
16
50
goal: 
[770, 570]
607.5397431080456
p: 
8
36
goal: 
[770, 570]
712.560733823463
p: 
8
39
goal: 
[770, 570]
705.5190602792671
p: 
10
41
goal: 
[770, 570]
684.9707237815683
p: 
20
35
goal: 
[770, 570]
606.6195975380847
p: 
22
37
goal: 
[770, 570]
578.2257424912702
p: 
22
16
goal: 
[770, 570]
681.6734535314472
p: 
20
17
goal: 
[770, 570]
690.4009564937627
p: 
19
20
goal: 
[770, 570]
683.4143590435647
p: 
25
17
goal: 
[770, 570]
648.1698912204441
p: 
22
16
goal: 
[770, 570]
674.0387819141802
p: 
20
17
goal: 
[770, 570]
690.4009659965757
p: 
22
28
goal: 
[770, 570]
610.5002757748141
p: 
15
39
goal: 
[770, 570]
644.3960222909236
p: 
17
20
goal: 
[770, 570]
700.645418514919
p: 
14
22
goal: 
[770, 570]
711.7418690058564
p: 
14
24
goal: 
[770, 570]
707.2020562625521
p: 
24
29
goal: 
[770, 570]
592.86282519932
p: 
17
20
goal: 
[770, 570]
700.645418514919
p: 
14
22
goal: 
[770, 570]
711.7418690058564
p: 
14
24
goal: 
[770, 570]
707.2020562625521
p: 
24
29
goal: 
[770, 570]
592.86282519932
p: 
12
37
goal: 
[770, 570]
669.1737383473935
p: 
12
40
goal: 
[770, 570]
669.0735410542327
p: 
13
42
goal: 
[770, 570]
653.9188912235918
p: 
24
39
goal: 
[770, 570]
555.2986263051544
p: 
16
32
goal: 
[770, 570]
655.0848380436837
p: 
18
34
goal: 
[770, 570]
628.7564816864727
p: 
21
34
goal: 
[770, 570]
603.0283217475111
p: 
22
23
goal: 
[770, 570]
643.5304195515619
p: 
21
40
goal: 
[770, 570]
576.9266108246396
p: 
24
39
goal: 
[770, 570]
554.254683061182
p: 
26
37
goal: 
[770, 570]
545.6859605993153
p: 
17
29
goal: 
[770, 570]
653.6727655030119
p: 
25
45
goal: 
[770, 570]
531.5979538342301
p: 
27
44
goal: 
[770, 570]
507.8911054126174
p: 
29
42
goal: 
[770, 570]
497.5190686802514
p: 
21
34
goal: 
[770, 570]
603.0283217475111
p: 
23
42
goal: 
[770, 570]
555.7101934863808
p: 
24
39
goal: 
[770, 570]
554.254683061182
p: 
23
50
goal: 
[770, 570]
541.7293225722608
p: 
25
50
goal: 
[770, 570]
514.4759858403727
p: 
27
39
goal: 
[770, 570]
528.1303496953813
p: 
26
56
goal: 
[770, 570]
503.4537003353058
p: 
29
55
goal: 
[770, 570]
477.3202370526723
p: 
30
53
goal: 
[770, 570]
461.4813742589034
p: 
36
56
goal: 
[770, 570]
409.7994541052139
p: 
36
53
goal: 
[770, 570]
401.5134823177539
p: 
36
51
goal: 
[770, 570]
411.5869796713155
p: 
24
53
goal: 
[770, 570]
521.4566603449566
p: 
42
56
goal: 
[770, 570]
349.829382946513
p: 
42
54
goal: 
[770, 570]
341.5568791625272
p: 
42
51
goal: 
[770, 570]
351.92160580435257
p: 
30
53
goal: 
[770, 570]
461.4813742589034
p: 
48
54
goal: 
[770, 570]
281.61877502899864
p: 
48
51
goal: 
[770, 570]
292.39322658732203
p: 
36
53
goal: 
[770, 570]
401.5134823177539
p: 
54
54
goal: 
[770, 570]
221.71471983398501
p: 
54
52
goal: 
[770, 570]
233.106848262681
p: 
42
54
goal: 
[770, 570]
341.5568791625272
p: 
60
54
goal: 
[770, 570]
161.88172514233034
p: 
60
52
goal: 
[770, 570]
174.31007241196232
p: 
48
54
goal: 
[770, 570]
281.61877502899864
p: 
54
54
goal: 
[770, 570]
221.71471983398501
p: 
56
56
goal: 
[770, 570]
205.44158036968054
p: 
59
49
goal: 
[770, 570]
189.89363183717936
p: 
50
56
goal: 
[770, 570]
265.40473758843785
p: 
53
49
goal: 
[770, 570]
247.0163773391112
p: 
53
49
goal: 
[770, 570]
247.01741321511773
p: 
44
56
goal: 
[770, 570]
325.38184487550285
p: 
58
52
goal: 
[770, 570]
190.61628774949625
p: 
59
49
goal: 
[770, 570]
189.89471718932091
p: 
47
49
goal: 
[770, 570]
305.2463309898675
p: 
53
49
goal: 
[770, 570]
247.01741321511773
p: 
38
51
goal: 
[770, 570]
386.9868808889917
p: 
47
49
goal: 
[770, 570]
305.2468898184421
p: 
38
56
goal: 
[770, 570]
385.36611026181595
p: 
52
51
goal: 
[770, 570]
249.5908973622056
p: 
53
49
goal: 
[770, 570]
247.01804240990447
p: 
41
48
goal: 
[770, 570]
364.05162424341364
p: 
58
52
goal: 
[770, 570]
190.61687099534558
p: 
59
49
goal: 
[770, 570]
189.8954084083648
p: 
47
49
goal: 
[770, 570]
305.24691931958824
p: 
53
49
goal: 
[770, 570]
247.01804240990447
p: 
55
56
goal: 
[770, 570]
210.84247985001136
p: 
57
54
goal: 
[770, 570]
195.20928799584235
p: 
62
52
goal: 
[770, 570]
148.5839288344516
p: 
51
54
goal: 
[770, 570]
255.08869244372192
p: 
52
51
goal: 
[770, 570]
249.5908973622056
p: 
32
51
goal: 
[770, 570]
446.7579205524721
p: 
41
48
goal: 
[770, 570]
364.05182677944185
p: 
32
56
goal: 
[770, 570]
445.3546232243818
p: 
46
51
goal: 
[770, 570]
308.96062930738606
p: 
47
49
goal: 
[770, 570]
305.24712413673984
p: 
35
48
goal: 
[770, 570]
423.1922223508102
p: 
52
51
goal: 
[770, 570]
249.59108082941376
p: 
53
49
goal: 
[770, 570]
247.01832302215257
p: 
41
48
goal: 
[770, 570]
364.05182677944185
p: 
58
52
goal: 
[770, 570]
190.61709963777423
p: 
59
49
goal: 
[770, 570]
189.8957618009729
p: 
47
49
goal: 
[770, 570]
305.2471536378633
p: 
53
49
goal: 
[770, 570]
247.01832302215257
p: 
55
56
goal: 
[770, 570]
210.84248143899225
p: 
57
54
goal: 
[770, 570]
195.20939760024032
p: 
62
52
goal: 
[770, 570]
148.5842302697059
p: 
51
54
goal: 
[770, 570]
255.0887855586522
p: 
52
51
goal: 
[770, 570]
249.59108082941376
p: 
49
56
goal: 
[770, 570]
270.8069819605276
p: 
51
54
goal: 
[770, 570]
255.08960379995708
p: 
57
54
goal: 
[770, 570]
195.21019773889466
p: 
56
52
goal: 
[770, 570]
206.98851667753365
p: 
45
54
goal: 
[770, 570]
315.01542029522085
p: 
62
52
goal: 
[770, 570]
148.58474160223645
p: 
51
54
goal: 
[770, 570]
255.08960379995708
p: 
62
49
goal: 
[770, 570]
165.25408579401306
p: 
53
56
goal: 
[770, 570]
238.85244326565882
p: 
56
49
goal: 
[770, 570]
221.53674292756892
p: 
46
51
goal: 
[770, 570]
308.96062930738606
p: 
25
50
goal: 
[770, 570]
514.4759894431056
p: 
28
51
goal: 
[770, 570]
487.2341312556487
p: 
25
45
goal: 
[770, 570]
531.5979538342301
p: 
31
40
goal: 
[770, 570]
488.4610491445729
p: 
32
37
goal: 
[770, 570]
489.2911848475825
p: 
31
34
goal: 
[770, 570]
506.92582735575706
p: 
20
37
goal: 
[770, 570]
602.7772974407
p: 
26
37
goal: 
[770, 570]
545.6859605993153
p: 
27
35
goal: 
[770, 570]
538.3727385212603
p: 
32
29
goal: 
[770, 570]
523.7870969911532
p: 
27
39
goal: 
[770, 570]
523.621423872674
p: 
31
23
goal: 
[770, 570]
568.9900958505675
p: 
28
24
goal: 
[770, 570]
579.4894237550186
p: 
23
34
goal: 
[770, 570]
577.4501704754565
p: 
32
29
goal: 
[770, 570]
523.7870969911532
p: 
24
20
goal: 
[770, 570]
635.5739063236872
p: 
23
22
goal: 
[770, 570]
638.3138335663573
p: 
22
25
goal: 
[770, 570]
625.6755900829062
p: 
14
38
goal: 
[770, 570]
655.3890403627895
p: 
16
40
goal: 
[770, 570]
629.8700847681386
p: 
19
40
goal: 
[770, 570]
603.3587402937746
p: 
20
28
goal: 
[770, 570]
633.3506327792123
p: 
24
42
goal: 
[770, 570]
547.1198513538022
p: 
15
35
goal: 
[770, 570]
650.6980549405267
p: 
29
40
goal: 
[770, 570]
503.7186934162267
p: 
18
42
goal: 
[770, 570]
605.8234081174334
p: 
30
34
goal: 
[770, 570]
514.0315078979177
p: 
25
45
goal: 
[770, 570]
527.0010338974677
p: 
31
29
goal: 
[770, 570]
530.4860085037607
p: 
29
29
goal: 
[770, 570]
554.6776630492745
p: 
26
30
goal: 
[770, 570]
567.7242494330877
p: 
32
40
goal: 
[770, 570]
477.4824090342326
p: 
28
33
goal: 
[770, 570]
541.3122468793653
p: 
30
23
goal: 
[770, 570]
575.3705821265067
p: 
27
23
goal: 
[770, 570]
598.586841869354
p: 
25
24
goal: 
[770, 570]
609.8743390153053
p: 
30
34
goal: 
[770, 570]
514.0315078979177
p: 
22
26
goal: 
[770, 570]
622.1611622018643
p: 
21
28
goal: 
[770, 570]
627.4218777423666
p: 
20
31
goal: 
[770, 570]
617.1284962635888
p: 
32
32
goal: 
[770, 570]
508.0978815077578
p: 
26
28
goal: 
[770, 570]
581.7010677825626
p: 
14
45
goal: 
[770, 570]
636.6614919335391
p: 
17
45
goal: 
[770, 570]
609.6230830195892
p: 
18
34
goal: 
[770, 570]
628.7564816864727
p: 
13
40
goal: 
[770, 570]
653.2440235077252
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
10
34
goal: 
[770, 570]
696.220036297461
p: 
8
36
goal: 
[770, 570]
712.5605584324786
p: 
7
39
goal: 
[770, 570]
714.0315550189152
p: 
20
22
goal: 
[770, 570]
666.7965068330542
p: 
17
21
goal: 
[770, 570]
693.4067385738508
p: 
14
22
goal: 
[770, 570]
711.7418557008998
p: 
17
33
goal: 
[770, 570]
639.9868399834471
p: 
20
22
goal: 
[770, 570]
666.7965068330542
p: 
17
21
goal: 
[770, 570]
693.4067385738508
p: 
14
22
goal: 
[770, 570]
711.7418557008998
p: 
17
33
goal: 
[770, 570]
639.9868399834471
p: 
7
35
goal: 
[770, 570]
723.2155298694549
p: 
7
38
goal: 
[770, 570]
716.026107397305
p: 
9
40
goal: 
[770, 570]
695.3666221665043
p: 
19
35
goal: 
[770, 570]
617.503301186551
p: 
24
13
goal: 
[770, 570]
676.7329826998647
p: 
22
12
goal: 
[770, 570]
702.1812317998333
p: 
19
13
goal: 
[770, 570]
717.5637595267707
p: 
22
24
goal: 
[770, 570]
633.7082234737376
p: 
24
13
goal: 
[770, 570]
676.7329826998647
p: 
22
12
goal: 
[770, 570]
702.1812317998333
p: 
19
13
goal: 
[770, 570]
717.5637595267707
p: 
22
24
goal: 
[770, 570]
633.7082234737376
p: 
24
13
goal: 
[770, 570]
676.7329826998647
p: 
22
12
goal: 
[770, 570]
702.1812413864833
p: 
19
13
goal: 
[770, 570]
717.563777933621
p: 
22
24
goal: 
[770, 570]
633.708231206809
p: 
24
13
goal: 
[770, 570]
676.7330022171861
p: 
22
12
goal: 
[770, 570]
702.1812605597837
p: 
19
13
goal: 
[770, 570]
717.5637963404723
p: 
22
24
goal: 
[770, 570]
633.7082466729528
p: 
17
15
goal: 
[770, 570]
726.1045329126795
p: 
15
16
goal: 
[770, 570]
735.5643895377237
p: 
14
19
goal: 
[770, 570]
729.2673390845185
p: 
24
24
goal: 
[770, 570]
615.8229935160731
p: 
58
54
goal: 
[770, 570]
184.60464482515155
p: 
57
51
goal: 
[770, 570]
198.73900123525908
p: 
55
49
goal: 
[770, 570]
224.6609491530426
p: 
53
52
goal: 
[770, 570]
244.1382641159195
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
58
54
goal: 
[770, 570]
184.60464482515155
p: 
57
51
goal: 
[770, 570]
198.73900123525908
p: 
55
49
goal: 
[770, 570]
224.6609491530426
p: 
53
52
goal: 
[770, 570]
244.1382641159195
p: 
53
55
goal: 
[770, 570]
240.14606448575006
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
15
51
goal: 
[770, 570]
621.6419830078512
p: 
16
40
goal: 
[770, 570]
629.8700847681386
p: 
20
32
goal: 
[770, 570]
619.120897640188
p: 
13
22
goal: 
[770, 570]
723.950172208679
p: 
13
24
goal: 
[770, 570]
711.4686362436887
p: 
15
27
goal: 
[770, 570]
687.4914272470261
p: 
25
21
goal: 
[770, 570]
630.6053059262363
p: 
29
29
goal: 
[770, 570]
554.6776630492745
p: 
30
9
goal: 
[770, 570]
667.6856339040382
p: 
27
8
goal: 
[770, 570]
692.0287764799858
p: 
24
9
goal: 
[770, 570]
705.1984105719725
p: 
30
9
goal: 
[770, 570]
667.6856339040382
p: 
27
8
goal: 
[770, 570]
692.0287764799858
p: 
24
9
goal: 
[770, 570]
705.1984105719725
p: 
30
9
goal: 
[770, 570]
667.6856556640341
p: 
27
8
goal: 
[770, 570]
692.0287978431916
p: 
24
9
goal: 
[770, 570]
705.1984311745588
p: 
17
31
goal: 
[770, 570]
644.2721382270984
p: 
15
32
goal: 
[770, 570]
664.1894344802653
p: 
13
34
goal: 
[770, 570]
670.3914374610032
p: 
22
42
goal: 
[770, 570]
563.1540528975767
p: 
54
56
goal: 
[770, 570]
225.45117011510897
p: 
57
56
goal: 
[770, 570]
198.1325062617451
p: 
59
54
goal: 
[770, 570]
177.671907518574
p: 
53
52
goal: 
[770, 570]
237.01584336174542
p: 
55
50
goal: 
[770, 570]
226.76031664421154
p: 
54
56
goal: 
[770, 570]
225.45214641403146
p: 
57
56
goal: 
[770, 570]
198.133482376915
p: 
59
54
goal: 
[770, 570]
177.6728762006093
p: 
53
52
goal: 
[770, 570]
237.01680581087237
p: 
55
50
goal: 
[770, 570]
226.7612552600814
p: 
10
37
goal: 
[770, 570]
690.0463568953326
p: 
13
38
goal: 
[770, 570]
664.4708433279435
p: 
15
38
goal: 
[770, 570]
638.0013921080877
p: 
17
27
goal: 
[770, 570]
668.1086106589474
p: 
16
44
goal: 
[770, 570]
616.7959381271854
p: 
20
41
goal: 
[770, 570]
581.6705702051038
p: 
12
33
goal: 
[770, 570]
685.4950219731156
p: 
25
44
goal: 
[770, 570]
525.6677176788484
p: 
26
41
goal: 
[770, 570]
523.387548082565
p: 
26
39
goal: 
[770, 570]
538.4991191598917
p: 
14
41
goal: 
[770, 570]
640.2708746906757
p: 
32
42
goal: 
[770, 570]
465.54095448415046
p: 
32
39
goal: 
[770, 570]
481.42718070360945
p: 
20
41
goal: 
[770, 570]
581.6705849214098
p: 
26
41
goal: 
[770, 570]
523.387548082565
p: 
26
50
goal: 
[770, 570]
507.6125072375513
p: 
22
39
goal: 
[770, 570]
571.6557335428394
p: 
24
55
goal: 
[770, 570]
523.0462949257877
p: 
27
55
goal: 
[770, 570]
495.6869092232633
p: 
24
50
goal: 
[770, 570]
532.705622552933
p: 
26
50
goal: 
[770, 570]
507.6125072375513
p: 
31
36
goal: 
[770, 570]
498.31020345213557
p: 
29
34
goal: 
[770, 570]
521.5468373650949
p: 
27
33
goal: 
[770, 570]
548.8262201270929
p: 
25
36
goal: 
[770, 570]
554.5495511078674
p: 
31
28
goal: 
[770, 570]
537.9935272746128
p: 
26
39
goal: 
[770, 570]
538.4991191598917
p: 
32
23
goal: 
[770, 570]
559.9590270517577
p: 
29
23
goal: 
[770, 570]
582.8251684271947
p: 
27
24
goal: 
[770, 570]
593.557684166364
p: 
32
34
goal: 
[770, 570]
496.37573714465145
p: 
28
27
goal: 
[770, 570]
564.9161756566042
p: 
25
27
goal: 
[770, 570]
589.2195206722566
p: 
23
29
goal: 
[770, 570]
602.4247697798559
p: 
28
39
goal: 
[770, 570]
512.2897372152456
p: 
28
27
goal: 
[770, 570]
564.9161756566042
p: 
32
23
goal: 
[770, 570]
559.9590270517577
p: 
24
32
goal: 
[770, 570]
576.1132809350106
p: 
28
27
goal: 
[770, 570]
564.9161756566042
p: 
31
28
goal: 
[770, 570]
537.9935272746128
p: 
24
21
goal: 
[770, 570]
632.731416781892
p: 
22
23
goal: 
[770, 570]
644.2685859039623
p: 
27
33
goal: 
[770, 570]
548.8262201270929
p: 
14
50
goal: 
[770, 570]
627.6999520201701
p: 
17
50
goal: 
[770, 570]
600.4329328981931
p: 
18
38
goal: 
[770, 570]
611.6102926017621
p: 
13
45
goal: 
[770, 570]
641.0798772163915
p: 
23
20
goal: 
[770, 570]
649.5194919859532
p: 
21
22
goal: 
[770, 570]
652.4750675606693
p: 
21
25
goal: 
[770, 570]
640.0093328792975
p: 
32
26
goal: 
[770, 570]
534.8810605454524
p: 
15
55
goal: 
[770, 570]
616.67384424968
p: 
16
44
goal: 
[770, 570]
616.7959381271854
p: 
19
24
goal: 
[770, 570]
656.7436313286075
p: 
17
27
goal: 
[770, 570]
662.1504855681169
p: 
17
29
goal: 
[770, 570]
651.9396383973642
p: 
29
31
goal: 
[770, 570]
542.7595956222182
p: 
10
35
goal: 
[770, 570]
700.9726791532258
p: 
20
29
goal: 
[770, 570]
630.1493236941991
p: 
8
42
goal: 
[770, 570]
695.3682829211514
p: 
13
44
goal: 
[770, 570]
643.7537210528876
p: 
15
33
goal: 
[770, 570]
663.5852228867932
p: 
14
50
goal: 
[770, 570]
627.6999520201701
p: 
17
49
goal: 
[770, 570]
602.5279804822209
p: 
13
44
goal: 
[770, 570]
643.7537210528876
p: 
15
55
goal: 
[770, 570]
616.67384424968
p: 
16
44
goal: 
[770, 570]
616.7959381271854
p: 
25
21
goal: 
[770, 570]
624.435092759938
p: 
24
18
goal: 
[770, 570]
646.680695713374
p: 
22
16
goal: 
[770, 570]
674.0387456846942
p: 
15
25
goal: 
[770, 570]
691.5484820510673
p: 
20
19
goal: 
[770, 570]
681.7739538530499
p: 
30
17
goal: 
[770, 570]
608.0250517731481
p: 
29
15
goal: 
[770, 570]
631.6444256752885
p: 
27
13
goal: 
[770, 570]
658.8653736420342
p: 
20
22
goal: 
[770, 570]
666.7965068330542
p: 
36
16
goal: 
[770, 570]
572.6116817302681
p: 
24
15
goal: 
[770, 570]
663.5602883994475
p: 
42
15
goal: 
[770, 570]
541.0775488465922
p: 
41
13
goal: 
[770, 570]
566.6187846672555
p: 
38
11
goal: 
[770, 570]
593.0804031334526
p: 
46
19
goal: 
[770, 570]
483.58609645283923
p: 
47
17
goal: 
[770, 570]
491.67178372217023
p: 
47
14
goal: 
[770, 570]
514.1369380032437
p: 
36
13
goal: 
[770, 570]
592.4429950555107
p: 
51
21
goal: 
[770, 570]
434.7743343614027
p: 
53
19
goal: 
[770, 570]
444.8792820263412
p: 
53
16
goal: 
[770, 570]
468.51893613053016
p: 
42
15
goal: 
[770, 570]
541.0775488465922
p: 
51
27
goal: 
[770, 570]
394.08193411544426
p: 
53
27
goal: 
[770, 570]
377.3770135054033
p: 
56
25
goal: 
[770, 570]
378.1631806425326
p: 
49
15
goal: 
[770, 570]
492.7924359487424
p: 
53
32
goal: 
[770, 570]
338.94289306507125
p: 
55
32
goal: 
[770, 570]
320.9333254664312
p: 
58
31
goal: 
[770, 570]
320.2951727388708
p: 
51
21
goal: 
[770, 570]
434.7743468420505
p: 
55
38
goal: 
[770, 570]
285.7692120879883
p: 
57
38
goal: 
[770, 570]
266.0504656675029
p: 
60
36
goal: 
[770, 570]
263.38311540801743
p: 
53
27
goal: 
[770, 570]
377.3770135054033
p: 
62
42
goal: 
[770, 570]
208.21193746546575
p: 
55
32
goal: 
[770, 570]
320.9333254664312
p: 
67
41
goal: 
[770, 570]
180.4947633893117
p: 
56
40
goal: 
[770, 570]
262.95630175528015
p: 
73
40
goal: 
[770, 570]
168.80639344693293
p: 
72
37
goal: 
[770, 570]
195.9995941847011
p: 
70
36
goal: 
[770, 570]
217.2646585583775
p: 
77
44
goal: 
[770, 570]
125.3341967319238
p: 
79
42
goal: 
[770, 570]
149.3164765100956
p: 
79
39
goal: 
[770, 570]
176.36310733186997
p: 
67
38
goal: 
[770, 570]
204.6842118642141
p: 
76
50
goal: 
[770, 570]
67.77720407441807
p: 
79
50
goal: 
[770, 570]
73.64385722624878
p: 
81
48
goal: 
[770, 570]
98.04502698494144
p: 
75
38
goal: 
[770, 570]
182.1915636026569
p: 
78
55
goal: 
[770, 570]
22.482731734914225
p: 
81
55
goal: 
[770, 570]
48.35306480421133
p: 
83
54
goal: 
[770, 570]
74.32683705949577
p: 
77
44
goal: 
[770, 570]
125.3341967319238
DONE
p: 
55
49
goal: 
[770, 570]
224.6609491530426
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
58
50
goal: 
[770, 570]
197.30283778506833
p: 
55
49
goal: 
[770, 570]
224.6609587094739
p: 
53
50
goal: 
[770, 570]
247.31136603726168
p: 
53
54
goal: 
[770, 570]
237.03624421760156
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
47
49
goal: 
[770, 570]
304.9861031709407
p: 
57
54
goal: 
[770, 570]
192.96702550376187
p: 
41
48
goal: 
[770, 570]
362.71372111273706
p: 
41
51
goal: 
[770, 570]
357.899874484659
p: 
43
53
goal: 
[770, 570]
339.6240369073888
p: 
53
48
goal: 
[770, 570]
255.2272221199033
p: 
45
48
goal: 
[770, 570]
330.2446597825461
p: 
35
50
goal: 
[770, 570]
415.73316812015366
p: 
35
53
goal: 
[770, 570]
412.7567798858745
p: 
37
55
goal: 
[770, 570]
395.7490402551265
p: 
47
49
goal: 
[770, 570]
304.9861031709407
p: 
46
52
goal: 
[770, 570]
308.61016681455493
p: 
39
49
goal: 
[770, 570]
382.17221205801553
p: 
30
52
goal: 
[770, 570]
470.43269219684277
p: 
30
55
goal: 
[770, 570]
468.8754053714191
p: 
41
51
goal: 
[770, 570]
357.899874484659
p: 
30
49
goal: 
[770, 570]
473.5683017455188
p: 
40
54
goal: 
[770, 570]
363.6403639874827
p: 
24
54
goal: 
[770, 570]
526.2888063524238
p: 
24
56
goal: 
[770, 570]
525.8518489876561
p: 
35
53
goal: 
[770, 570]
412.7567798858745
p: 
27
47
goal: 
[770, 570]
503.8036121185505
p: 
25
48
goal: 
[770, 570]
522.8626736782492
p: 
24
51
goal: 
[770, 570]
528.1446651107995
p: 
35
55
goal: 
[770, 570]
420.03389436409276
p: 
24
48
goal: 
[770, 570]
531.4046643136595
p: 
24
51
goal: 
[770, 570]
528.1446798019249
p: 
26
53
goal: 
[770, 570]
510.6314763708504
p: 
27
41
goal: 
[770, 570]
518.8065997432988
p: 
24
42
goal: 
[770, 570]
541.3135592973259
p: 
27
53
goal: 
[770, 570]
495.6570120122887
p: 
30
55
goal: 
[770, 570]
468.8754053714191
p: 
30
52
goal: 
[770, 570]
470.43269219684277
p: 
30
36
goal: 
[770, 570]
512.8927499878538
p: 
27
35
goal: 
[770, 570]
540.0948956487141
p: 
24
36
goal: 
[770, 570]
560.8561010503241
p: 
27
47
goal: 
[770, 570]
503.8036121185505
p: 
32
30
goal: 
[770, 570]
513.467397315524
p: 
25
39
goal: 
[770, 570]
544.8875007592205
p: 
30
49
goal: 
[770, 570]
473.5682245135111
p: 
30
49
goal: 
[770, 570]
473.56829700322476
p: 
32
24
goal: 
[770, 570]
546.4292697122469
p: 
30
25
goal: 
[770, 570]
563.0280445180705
p: 
32
36
goal: 
[770, 570]
485.70833782094405
p: 
29
52
goal: 
[770, 570]
478.9542403620736
p: 
30
30
goal: 
[770, 570]
540.1834563558381
p: 
27
29
goal: 
[770, 570]
566.9609375340375
p: 
24
30
goal: 
[770, 570]
585.9170271520454
p: 
27
41
goal: 
[770, 570]
518.8065997432988
p: 
22
36
goal: 
[770, 570]
582.1629864263955
p: 
20
38
goal: 
[770, 570]
597.9070155813675
p: 
19
41
goal: 
[770, 570]
598.8345488148099
p: 
32
24
goal: 
[770, 570]
546.4292517760291
p: 
25
33
goal: 
[770, 570]
566.8887996477881
p: 
32
30
goal: 
[770, 570]
513.467381793955
p: 
32
30
goal: 
[770, 570]
513.467397315524
p: 
30
24
goal: 
[770, 570]
572.4835020033885
p: 
27
23
goal: 
[770, 570]
598.6542517081472
p: 
24
24
goal: 
[770, 570]
615.8229935160731
p: 
27
35
goal: 
[770, 570]
540.0948956487141
p: 
22
30
goal: 
[770, 570]
605.5162488521892
p: 
20
32
goal: 
[770, 570]
619.120897640188
p: 
19
35
goal: 
[770, 570]
617.503301186551
p: 
29
39
goal: 
[770, 570]
502.99947598944834
p: 
25
27
goal: 
[770, 570]
594.1576460103994
p: 
25
22
goal: 
[770, 570]
622.9673126201377
p: 
24
24
goal: 
[770, 570]
616.2961925945627
p: 
22
24
goal: 
[770, 570]
633.7082466729528
p: 
20
26
goal: 
[770, 570]
645.235284623566
p: 
19
29
goal: 
[770, 570]
641.2626896315013
p: 
29
33
goal: 
[770, 570]
526.7532434259444
p: 
24
31
goal: 
[770, 570]
578.4185506756148
p: 
22
30
goal: 
[770, 570]
605.5162488521892
p: 
19
31
goal: 
[770, 570]
625.6981937043336
p: 
22
42
goal: 
[770, 570]
564.2495528760835
p: 
27
29
goal: 
[770, 570]
566.9609375340375
p: 
30
30
goal: 
[770, 570]
532.4562956222243
p: 
29
28
goal: 
[770, 570]
553.1567591174371
p: 
27
26
goal: 
[770, 570]
580.442397371286
p: 
20
35
goal: 
[770, 570]
608.5671628422162
p: 
24
28
goal: 
[770, 570]
591.1851398097571
p: 
24
31
goal: 
[770, 570]
578.4185506756148
p: 
17
33
goal: 
[770, 570]
639.9868399834471
p: 
15
34
goal: 
[770, 570]
655.1070456415424
p: 
14
37
goal: 
[770, 570]
655.1887143583667
p: 
24
42
goal: 
[770, 570]
541.3135592973259
p: 
13
40
goal: 
[770, 570]
656.4117464534745
p: 
13
42
goal: 
[770, 570]
650.2376424542192
p: 
15
45
goal: 
[770, 570]
630.354756522152
p: 
25
39
goal: 
[770, 570]
549.1781311501051
p: 
24
21
goal: 
[770, 570]
630.4367566398764
p: 
27
32
goal: 
[770, 570]
551.3467343679742
p: 
24
25
goal: 
[770, 570]
607.0429884173362
p: 
22
24
goal: 
[770, 570]
633.7082234737376
p: 
19
25
goal: 
[770, 570]
652.2510273789436
p: 
22
36
goal: 
[770, 570]
582.1629864263955
p: 
24
25
goal: 
[770, 570]
607.0429884173362
p: 
22
24
goal: 
[770, 570]
633.7082234737376
p: 
19
25
goal: 
[770, 570]
652.2510273789436
p: 
22
36
goal: 
[770, 570]
582.1629864263955
p: 
22
18
goal: 
[770, 570]
666.1248449199436
p: 
20
20
goal: 
[770, 570]
675.682217589603
p: 
19
23
goal: 
[770, 570]
669.5710173429354
p: 
29
27
goal: 
[770, 570]
555.9941421354478
p: 
17
27
goal: 
[770, 570]
664.5284269452044
p: 
15
28
goal: 
[770, 570]
677.6885847273121
p: 
14
31
goal: 
[770, 570]
675.4690603956361
p: 
24
36
goal: 
[770, 570]
560.8561010503241
p: 
30
24
goal: 
[770, 570]
564.4565443456964
p: 
20
29
goal: 
[770, 570]
632.462244612667
p: 
24
22
goal: 
[770, 570]
621.8646997470436
p: 
30
24
goal: 
[770, 570]
564.4565443456964
p: 
20
29
goal: 
[770, 570]
632.462244612667
p: 
24
22
goal: 
[770, 570]
621.8646997470436
p: 
13
34
goal: 
[770, 570]
674.3531749165058
p: 
13
36
goal: 
[770, 570]
665.8842751414678
p: 
15
39
goal: 
[770, 570]
644.3960222909236
p: 
25
33
goal: 
[770, 570]
571.3306956232685
p: 
22
16
goal: 
[770, 570]
674.0387146800459
p: 
20
18
goal: 
[770, 570]
682.9172559234133
p: 
19
21
goal: 
[770, 570]
676.0959228722944
p: 
30
25
goal: 
[770, 570]
563.0280445180705
p: 
17
26
goal: 
[770, 570]
671.3969243294447
p: 
14
28
goal: 
[770, 570]
684.3717008883295
p: 
14
30
goal: 
[770, 570]
681.9334731145997
p: 
24
35
goal: 
[770, 570]
567.3022531230071
p: 
24
19
goal: 
[770, 570]
640.0268430485623
p: 
22
18
goal: 
[770, 570]
666.1248361887899
p: 
19
19
goal: 
[770, 570]
683.0553241458532
p: 
22
30
goal: 
[770, 570]
605.5162488521892
p: 
24
19
goal: 
[770, 570]
640.0268430485623
p: 
22
18
goal: 
[770, 570]
666.1248361887899
p: 
19
19
goal: 
[770, 570]
683.0553241458532
p: 
22
30
goal: 
[770, 570]
605.5162488521892
p: 
24
19
goal: 
[770, 570]
640.0268608243176
p: 
22
18
goal: 
[770, 570]
666.1248623822516
p: 
19
19
goal: 
[770, 570]
683.0553574580434
p: 
22
30
goal: 
[770, 570]
605.5162751767275
p: 
18
23
goal: 
[770, 570]
670.3226965167107
p: 
18
26
goal: 
[770, 570]
657.4919894564681
p: 
20
28
goal: 
[770, 570]
633.3506327792123
p: 
17
21
goal: 
[770, 570]
693.4067778336986
p: 
15
22
goal: 
[770, 570]
704.6689964127214
p: 
14
25
goal: 
[770, 570]
700.317536333373
p: 
24
30
goal: 
[770, 570]
585.9170271520454
p: 
13
50
goal: 
[770, 570]
641.9557673721371
p: 
15
50
goal: 
[770, 570]
614.6657400760107
p: 
17
39
goal: 
[770, 570]
624.3292016877002
p: 
16
56
goal: 
[770, 570]
604.1290012751683
p: 
55
49
goal: 
[770, 570]
230.7841750590744
p: 
53
50
goal: 
[770, 570]
247.3113583873292
p: 
52
53
goal: 
[770, 570]
250.78465849818733
p: 
20
28
goal: 
[770, 570]
637.4995854874331
p: 
17
27
goal: 
[770, 570]
664.5284269452044
p: 
14
28
goal: 
[770, 570]
684.3716870512048
p: 
17
39
goal: 
[770, 570]
620.2969293014565
p: 
13
28
goal: 
[770, 570]
697.0136372655293
p: 
13
30
goal: 
[770, 570]
686.4362636924294
p: 
15
33
goal: 
[770, 570]
663.5852228867932
p: 
25
27
goal: 
[770, 570]
598.6993467545302
p: 
9
33
goal: 
[770, 570]
712.1388266605404
p: 
20
38
goal: 
[770, 570]
597.9070155813675
p: 
25
27
goal: 
[770, 570]
592.063350796343
p: 
24
24
goal: 
[770, 570]
612.9479004654312
p: 
22
22
goal: 
[770, 570]
640.2495051471956
p: 
15
31
goal: 
[770, 570]
666.5631111443294
p: 
30
31
goal: 
[770, 570]
536.0197311384238
p: 
31
28
goal: 
[770, 570]
533.8134889823411
p: 
31
26
goal: 
[770, 570]
548.9657003126724
p: 
20
25
goal: 
[770, 570]
650.6313802606566
p: 
25
27
goal: 
[770, 570]
592.063350796343
p: 
29
36
goal: 
[770, 570]
517.7284558359863
p: 
32
36
goal: 
[770, 570]
492.94303227760696
p: 
28
25
goal: 
[770, 570]
582.1008637609626
p: 
31
42
goal: 
[770, 570]
479.4949891422897
p: 
30
31
goal: 
[770, 570]
536.0197311384238
p: 
24
39
goal: 
[770, 570]
555.2986263051544
p: 
25
41
goal: 
[770, 570]
532.7896451118836
p: 
28
42
goal: 
[770, 570]
505.43004852508744
p: 
32
31
goal: 
[770, 570]
509.3335017527707
p: 
26
37
goal: 
[770, 570]
542.7613493882569
p: 
25
47
goal: 
[770, 570]
526.7623308990517
p: 
29
36
goal: 
[770, 570]
517.7284558359863
p: 
24
53
goal: 
[770, 570]
527.0516285526195
p: 
27
53
goal: 
[770, 570]
499.8267448837046
p: 
29
51
goal: 
[770, 570]
479.65476161119824
p: 
23
41
goal: 
[770, 570]
558.8651349971341
p: 
33
55
goal: 
[770, 570]
435.14356155008886
p: 
35
53
goal: 
[770, 570]
420.8357554592968
p: 
35
50
goal: 
[770, 570]
424.39006867227914
p: 
23
49
goal: 
[770, 570]
538.7343807423359
p: 
40
55
goal: 
[770, 570]
362.4041405753585
p: 
40
52
goal: 
[770, 570]
365.1547423639145
p: 
29
51
goal: 
[770, 570]
479.65476161119824
p: 
46
56
goal: 
[770, 570]
304.5829516499516
p: 
46
54
goal: 
[770, 570]
306.2172803420159
p: 
35
53
goal: 
[770, 570]
420.8357554592968
p: 
40
55
goal: 
[770, 570]
362.4041405753585
p: 
52
53
goal: 
[770, 570]
250.78350905659104
p: 
51
50
goal: 
[770, 570]
264.4772807881511
p: 
49
49
goal: 
[770, 570]
290.0597248541102
p: 
57
54
goal: 
[770, 570]
191.6266005980359
p: 
57
52
goal: 
[770, 570]
196.74049494450463
p: 
46
51
goal: 
[770, 570]
310.26476406566184
p: 
52
53
goal: 
[770, 570]
250.78350905659104
p: 
62
48
goal: 
[770, 570]
165.1661382463377
p: 
53
55
goal: 
[770, 570]
239.4445648997239
p: 
57
52
goal: 
[770, 570]
196.74049494450463
p: 
57
49
goal: 
[770, 570]
212.76401765071006
p: 
46
54
goal: 
[770, 570]
306.2172803420159
p: 
61
53
goal: 
[770, 570]
161.4449678744656
p: 
62
51
goal: 
[770, 570]
152.890305478055
p: 
62
48
goal: 
[770, 570]
165.1663844657902
p: 
57
49
goal: 
[770, 570]
212.7640282007394
p: 
57
52
goal: 
[770, 570]
196.74061316186828
p: 
49
55
goal: 
[770, 570]
279.57006359296633
p: 
46
51
goal: 
[770, 570]
310.26494421535347
p: 
45
48
goal: 
[770, 570]
324.4047038485055
p: 
35
55
goal: 
[770, 570]
410.654940869005
p: 
50
55
goal: 
[770, 570]
263.9982556948795
p: 
52
53
goal: 
[770, 570]
250.78369005909417
p: 
52
50
goal: 
[770, 570]
256.67446835587265
p: 
40
49
goal: 
[770, 570]
369.9140292653391
p: 
57
54
goal: 
[770, 570]
191.62678267570013
p: 
57
52
goal: 
[770, 570]
196.740672602464
p: 
46
51
goal: 
[770, 570]
310.26494421535347
p: 
52
53
goal: 
[770, 570]
250.78369005909417
p: 
62
48
goal: 
[770, 570]
165.1662963678273
p: 
53
55
goal: 
[770, 570]
239.444747775941
p: 
57
52
goal: 
[770, 570]
196.740672602464
p: 
57
49
goal: 
[770, 570]
205.40281956353326
p: 
47
54
goal: 
[770, 570]
297.972119588014
p: 
62
53
goal: 
[770, 570]
153.53714310162766
p: 
48
49
goal: 
[770, 570]
292.4681744145681
p: 
40
52
goal: 
[770, 570]
365.1547423639145
p: 
40
49
goal: 
[770, 570]
369.9138602969119
p: 
30
54
goal: 
[770, 570]
468.70581279434094
p: 
44
53
goal: 
[770, 570]
322.5989288964181
p: 
46
51
goal: 
[770, 570]
310.2647913020902
p: 
46
48
goal: 
[770, 570]
316.63338880156596
p: 
50
55
goal: 
[770, 570]
263.99820568531607
p: 
52
53
goal: 
[770, 570]
250.78356092734836
p: 
52
50
goal: 
[770, 570]
256.67425111310575
p: 
40
49
goal: 
[770, 570]
369.9138602969119
p: 
57
54
goal: 
[770, 570]
191.6266922674326
p: 
57
52
goal: 
[770, 570]
196.7404657250095
p: 
46
51
goal: 
[770, 570]
310.2647913020902
p: 
52
53
goal: 
[770, 570]
250.78356092734836
p: 
62
48
goal: 
[770, 570]
165.16586548678816
p: 
53
55
goal: 
[770, 570]
239.4447050317546
p: 
57
52
goal: 
[770, 570]
196.7404657250095
p: 
57
49
goal: 
[770, 570]
205.40250760222918
p: 
47
54
goal: 
[770, 570]
297.97203469914535
p: 
62
53
goal: 
[770, 570]
153.53694877389736
p: 
48
49
goal: 
[770, 570]
292.467963903312
p: 
41
52
goal: 
[770, 570]
356.9888720262011
p: 
42
48
goal: 
[770, 570]
352.40776186200844
p: 
31
49
goal: 
[770, 570]
460.22579024955104
p: 
25
47
goal: 
[770, 570]
526.7623254675968
p: 
26
29
goal: 
[770, 570]
571.7250761305163
p: 
27
48
goal: 
[770, 570]
499.5670918944992
p: 
18
37
goal: 
[770, 570]
612.8173096663437
p: 
18
39
goal: 
[770, 570]
611.8888586415121
p: 
19
42
goal: 
[770, 570]
596.1220649344363
p: 
30
39
goal: 
[770, 570]
499.50529804121174
p: 
30
23
goal: 
[770, 570]
570.9950437160629
p: 
20
28
goal: 
[770, 570]
637.4995854874331
p: 
19
41
goal: 
[770, 570]
598.8345488148099
p: 
27
14
goal: 
[770, 570]
651.4396933671469
p: 
20
23
goal: 
[770, 570]
660.9558845938947
p: 
27
14
goal: 
[770, 570]
651.4396933671469
p: 
20
23
goal: 
[770, 570]
660.9558845938947
p: 
27
14
goal: 
[770, 570]
651.4397132506427
p: 
20
23
goal: 
[770, 570]
660.9559001605792
p: 
58
50
goal: 
[770, 570]
197.30283778506833
p: 
55
49
goal: 
[770, 570]
224.6609587094739
p: 
53
50
goal: 
[770, 570]
247.31136603726168
p: 
53
54
goal: 
[770, 570]
237.03624421760156
p: 
15
45
goal: 
[770, 570]
630.354756522152
p: 
13
44
goal: 
[770, 570]
650.5492713393085
p: 
15
44
goal: 
[770, 570]
623.5622456258719
p: 
17
33
goal: 
[770, 570]
643.7996845687106
p: 
16
50
goal: 
[770, 570]
607.5397431080456
p: 
12
39
goal: 
[770, 570]
667.6298394818576
p: 
14
56
goal: 
[770, 570]
624.0725076007941
p: 
17
56
goal: 
[770, 570]
596.7162039869553
p: 
13
51
goal: 
[770, 570]
632.910736716354
p: 
16
50
goal: 
[770, 570]
607.5397431080456
p: 
8
36
goal: 
[770, 570]
712.560733823463
p: 
8
39
goal: 
[770, 570]
705.5190602792671
p: 
10
41
goal: 
[770, 570]
684.9707237815683
p: 
20
35
goal: 
[770, 570]
606.6195975380847
p: 
22
37
goal: 
[770, 570]
578.2257424912702
p: 
22
16
goal: 
[770, 570]
681.6734535314472
p: 
20
17
goal: 
[770, 570]
690.4009564937627
p: 
19
20
goal: 
[770, 570]
683.4143590435647
p: 
25
17
goal: 
[770, 570]
648.1698912204441
p: 
22
16
goal: 
[770, 570]
674.0387819141802
p: 
20
17
goal: 
[770, 570]
690.4009659965757
p: 
22
28
goal: 
[770, 570]
610.5002757748141
p: 
15
39
goal: 
[770, 570]
644.3960222909236
p: 
17
20
goal: 
[770, 570]
700.645418514919
p: 
14
22
goal: 
[770, 570]
711.7418690058564
p: 
14
24
goal: 
[770, 570]
707.2020562625521
p: 
24
29
goal: 
[770, 570]
592.86282519932
p: 
17
20
goal: 
[770, 570]
700.645418514919
p: 
14
22
goal: 
[770, 570]
711.7418690058564
p: 
14
24
goal: 
[770, 570]
707.2020562625521
p: 
24
29
goal: 
[770, 570]
592.86282519932
p: 
12
37
goal: 
[770, 570]
669.1737383473935
p: 
12
40
goal: 
[770, 570]
669.0735410542327
p: 
13
42
goal: 
[770, 570]
653.9188912235918
p: 
24
39
goal: 
[770, 570]
555.2986263051544
p: 
16
32
goal: 
[770, 570]
655.0848380436837
p: 
18
34
goal: 
[770, 570]
628.7564816864727
p: 
21
34
goal: 
[770, 570]
603.0283217475111
p: 
22
23
goal: 
[770, 570]
643.5304195515619
p: 
21
40
goal: 
[770, 570]
576.9266108246396
p: 
24
39
goal: 
[770, 570]
554.254683061182
p: 
26
37
goal: 
[770, 570]
545.6859605993153
p: 
17
29
goal: 
[770, 570]
653.6727655030119
p: 
25
45
goal: 
[770, 570]
531.5979538342301
p: 
27
44
goal: 
[770, 570]
507.8911054126174
p: 
29
42
goal: 
[770, 570]
497.5190686802514
p: 
21
34
goal: 
[770, 570]
603.0283217475111
p: 
23
42
goal: 
[770, 570]
555.7101934863808
p: 
24
39
goal: 
[770, 570]
554.254683061182
p: 
23
50
goal: 
[770, 570]
541.7293225722608
p: 
25
50
goal: 
[770, 570]
514.4759858403727
p: 
27
39
goal: 
[770, 570]
528.1303496953813
p: 
26
56
goal: 
[770, 570]
503.4537003353058
p: 
29
55
goal: 
[770, 570]
477.3202370526723
p: 
30
53
goal: 
[770, 570]
461.4813742589034
p: 
36
56
goal: 
[770, 570]
409.7994541052139
p: 
36
53
goal: 
[770, 570]
401.5134823177539
p: 
36
51
goal: 
[770, 570]
411.5869796713155
p: 
24
53
goal: 
[770, 570]
521.4566603449566
p: 
42
56
goal: 
[770, 570]
349.829382946513
p: 
42
54
goal: 
[770, 570]
341.5568791625272
p: 
42
51
goal: 
[770, 570]
351.92160580435257
p: 
30
53
goal: 
[770, 570]
461.4813742589034
p: 
48
54
goal: 
[770, 570]
281.61877502899864
p: 
48
51
goal: 
[770, 570]
292.39322658732203
p: 
36
53
goal: 
[770, 570]
401.5134823177539
p: 
54
54
goal: 
[770, 570]
221.71471983398501
p: 
54
52
goal: 
[770, 570]
233.106848262681
p: 
42
54
goal: 
[770, 570]
341.5568791625272
p: 
60
54
goal: 
[770, 570]
161.88172514233034
p: 
60
52
goal: 
[770, 570]
174.31007241196232
p: 
48
54
goal: 
[770, 570]
281.61877502899864
p: 
54
54
goal: 
[770, 570]
221.71471983398501
p: 
56
56
goal: 
[770, 570]
205.44158036968054
p: 
59
49
goal: 
[770, 570]
189.89363183717936
p: 
50
56
goal: 
[770, 570]
265.40473758843785
p: 
53
49
goal: 
[770, 570]
247.0163773391112
p: 
53
49
goal: 
[770, 570]
247.01741321511773
p: 
44
56
goal: 
[770, 570]
325.38184487550285
p: 
58
52
goal: 
[770, 570]
190.61628774949625
p: 
59
49
goal: 
[770, 570]
189.89471718932091
p: 
47
49
goal: 
[770, 570]
305.2463309898675
p: 
53
49
goal: 
[770, 570]
247.01741321511773
p: 
38
51
goal: 
[770, 570]
386.9868808889917
p: 
47
49
goal: 
[770, 570]
305.2468898184421
p: 
38
56
goal: 
[770, 570]
385.36611026181595
p: 
52
51
goal: 
[770, 570]
249.5908973622056
p: 
53
49
goal: 
[770, 570]
247.01804240990447
p: 
41
48
goal: 
[770, 570]
364.05162424341364
p: 
58
52
goal: 
[770, 570]
190.61687099534558
p: 
59
49
goal: 
[770, 570]
189.8954084083648
p: 
47
49
goal: 
[770, 570]
305.24691931958824
p: 
53
49
goal: 
[770, 570]
247.01804240990447
p: 
55
56
goal: 
[770, 570]
210.84247985001136
p: 
57
54
goal: 
[770, 570]
195.20928799584235
p: 
62
52
goal: 
[770, 570]
148.5839288344516
p: 
51
54
goal: 
[770, 570]
255.08869244372192
p: 
52
51
goal: 
[770, 570]
249.5908973622056
p: 
32
51
goal: 
[770, 570]
446.7579205524721
p: 
41
48
goal: 
[770, 570]
364.05182677944185
p: 
32
56
goal: 
[770, 570]
445.3546232243818
p: 
46
51
goal: 
[770, 570]
308.96062930738606
p: 
47
49
goal: 
[770, 570]
305.24712413673984
p: 
35
48
goal: 
[770, 570]
423.1922223508102
p: 
52
51
goal: 
[770, 570]
249.59108082941376
p: 
53
49
goal: 
[770, 570]
247.01832302215257
p: 
41
48
goal: 
[770, 570]
364.05182677944185
p: 
58
52
goal: 
[770, 570]
190.61709963777423
p: 
59
49
goal: 
[770, 570]
189.8957618009729
p: 
47
49
goal: 
[770, 570]
305.2471536378633
p: 
53
49
goal: 
[770, 570]
247.01832302215257
p: 
55
56
goal: 
[770, 570]
210.84248143899225
p: 
57
54
goal: 
[770, 570]
195.20939760024032
p: 
62
52
goal: 
[770, 570]
148.5842302697059
p: 
51
54
goal: 
[770, 570]
255.0887855586522
p: 
52
51
goal: 
[770, 570]
249.59108082941376
p: 
49
56
goal: 
[770, 570]
270.8069819605276
p: 
51
54
goal: 
[770, 570]
255.08960379995708
p: 
57
54
goal: 
[770, 570]
195.21019773889466
p: 
56
52
goal: 
[770, 570]
206.98851667753365
p: 
45
54
goal: 
[770, 570]
315.01542029522085
p: 
62
52
goal: 
[770, 570]
148.58474160223645
p: 
51
54
goal: 
[770, 570]
255.08960379995708
p: 
62
49
goal: 
[770, 570]
165.25408579401306
p: 
53
56
goal: 
[770, 570]
238.85244326565882
p: 
56
49
goal: 
[770, 570]
221.53674292756892
p: 
46
51
goal: 
[770, 570]
308.96062930738606
p: 
25
50
goal: 
[770, 570]
514.4759894431056
p: 
28
51
goal: 
[770, 570]
487.2341312556487
p: 
25
45
goal: 
[770, 570]
531.5979538342301
p: 
31
40
goal: 
[770, 570]
488.4610491445729
p: 
32
37
goal: 
[770, 570]
489.2911848475825
p: 
31
34
goal: 
[770, 570]
506.92582735575706
p: 
20
37
goal: 
[770, 570]
602.7772974407
p: 
26
37
goal: 
[770, 570]
545.6859605993153
p: 
27
35
goal: 
[770, 570]
538.3727385212603
p: 
32
29
goal: 
[770, 570]
523.7870969911532
p: 
27
39
goal: 
[770, 570]
523.621423872674
p: 
31
23
goal: 
[770, 570]
568.9900958505675
p: 
28
24
goal: 
[770, 570]
579.4894237550186
p: 
23
34
goal: 
[770, 570]
577.4501704754565
p: 
32
29
goal: 
[770, 570]
523.7870969911532
p: 
24
20
goal: 
[770, 570]
635.5739063236872
p: 
23
22
goal: 
[770, 570]
638.3138335663573
p: 
22
25
goal: 
[770, 570]
625.6755900829062
p: 
14
38
goal: 
[770, 570]
655.3890403627895
p: 
16
40
goal: 
[770, 570]
629.8700847681386
p: 
19
40
goal: 
[770, 570]
603.3587402937746
p: 
20
28
goal: 
[770, 570]
633.3506327792123
p: 
24
42
goal: 
[770, 570]
547.1198513538022
p: 
15
35
goal: 
[770, 570]
650.6980549405267
p: 
29
40
goal: 
[770, 570]
503.7186934162267
p: 
18
42
goal: 
[770, 570]
605.8234081174334
p: 
30
34
goal: 
[770, 570]
514.0315078979177
p: 
25
45
goal: 
[770, 570]
527.0010338974677
p: 
31
29
goal: 
[770, 570]
530.4860085037607
p: 
29
29
goal: 
[770, 570]
554.6776630492745
p: 
26
30
goal: 
[770, 570]
567.7242494330877
p: 
32
40
goal: 
[770, 570]
477.4824090342326
p: 
28
33
goal: 
[770, 570]
541.3122468793653
p: 
30
23
goal: 
[770, 570]
575.3705821265067
p: 
27
23
goal: 
[770, 570]
598.586841869354
p: 
25
24
goal: 
[770, 570]
609.8743390153053
p: 
30
34
goal: 
[770, 570]
514.0315078979177
p: 
22
26
goal: 
[770, 570]
622.1611622018643
p: 
21
28
goal: 
[770, 570]
627.4218777423666
p: 
20
31
goal: 
[770, 570]
617.1284962635888
p: 
32
32
goal: 
[770, 570]
508.0978815077578
p: 
26
28
goal: 
[770, 570]
581.7010677825626
p: 
14
45
goal: 
[770, 570]
636.6614919335391
p: 
17
45
goal: 
[770, 570]
609.6230830195892
p: 
18
34
goal: 
[770, 570]
628.7564816864727
p: 
13
40
goal: 
[770, 570]
653.2440235077252
p: 
55
55
goal: 
[770, 570]
213.6163123771495
p: 
10
34
goal: 
[770, 570]
696.220036297461
p: 
8
36
goal: 
[770, 570]
712.5605584324786
p: 
7
39
goal: 
[770, 570]
714.0315550189152
p: 
20
22
goal: 
[770, 570]
666.7965068330542
p: 
17
21
goal: 
[770, 570]
693.4067385738508
p: 
14
22
goal: 
[770, 570]
711.7418557008998
p: 
17
33
goal: 
[770, 570]
639.9868399834471
p: 
20
22
goal: 
[770, 570]
666.7965068330542
p: 
17
21
goal: 
[770, 570]
693.4067385738508
p: 
14
22
goal: 
[770, 570]
711.7418557008998
p: 
17
33
goal: 
[770, 570]
639.9868399834471
p: 
7
35
goal: 
[770, 570]
723.2155298694549
p: 
7
38
goal: 
[770, 570]
716.026107397305
p: 
9
40
goal: 
[770, 570]
695.3666221665043
p: 
19
35
goal: 
[770, 570]
617.503301186551
p: 
24
13
goal: 
[770, 570]
676.7329826998647
p: 
22
12
goal: 
[770, 570]
702.1812317998333
p: 
19
13
goal: 
[770, 570]
717.5637595267707
p: 
22
24
goal: 
[770, 570]
633.7082234737376
p: 
24
13
goal: 
[770, 570]
676.7329826998647
p: 
22
12
goal: 
[770, 570]
702.1812317998333
p: 
19
13
goal: 
[770, 570]
717.5637595267707
p: 
22
24
goal: 
[770, 570]
633.7082234737376
p: 
24
13
goal: 
[770, 570]
676.7329826998647
p: 
22
12
goal: 
[770, 570]
702.1812413864833
p: 
19
13
goal: 
[770, 570]
717.563777933621
p: 
22
24
goal: 
[770, 570]
633.708231206809
p: 
24
13
goal: 
[770, 570]
676.7330022171861
p: 
22
12
goal: 
[770, 570]
702.1812605597837
p: 
19
13
goal: 
[770, 570]
717.5637963404723
p: 
22
24
goal: 
[770, 570]
633.7082466729528
p: 
17
15
goal: 
[770, 570]
726.1045329126795
p: 
15
16
goal: 
[770, 570]
735.5643895377237
p: 
14
19
goal: 
[770, 570]
729.2673390845185
p: 
24
24
goal: 
[770, 570]
615.8229935160731
p: 
15
51
goal: 
[770, 570]
621.6419830078512
p: 
16
40
goal: 
[770, 570]
629.8700847681386
p: 
20
32
goal: 
[770, 570]
619.120897640188
p: 
13
22
goal: 
[770, 570]
723.950172208679
p: 
13
24
goal: 
[770, 570]
711.4686362436887
p: 
15
27
goal: 
[770, 570]
687.4914272470261
p: 
25
21
goal: 
[770, 570]
630.6053059262363
p: 
29
29
goal: 
[770, 570]
554.6776630492745
p: 
30
9
goal: 
[770, 570]
667.6856339040382
p: 
27
8
goal: 
[770, 570]
692.0287764799858
p: 
24
9
goal: 
[770, 570]
705.1984105719725
p: 
30
9
goal: 
[770, 570]
667.6856339040382
p: 
27
8
goal: 
[770, 570]
692.0287764799858
p: 
24
9
goal: 
[770, 570]
705.1984105719725
p: 
30
9
goal: 
[770, 570]
667.6856556640341
p: 
27
8
goal: 
[770, 570]
692.0287978431916
p: 
24
9
goal: 
[770, 570]
705.1984311745588
p: 
17
31
goal: 
[770, 570]
644.2721382270984
p: 
15
32
goal: 
[770, 570]
664.1894344802653
p: 
13
34
goal: 
[770, 570]
670.3914374610032
p: 
22
42
goal: 
[770, 570]
563.1540528975767
p: 
10
37
goal: 
[770, 570]
690.0463568953326
p: 
13
38
goal: 
[770, 570]
664.4708433279435
p: 
15
38
goal: 
[770, 570]
638.0013921080877
p: 
17
27
goal: 
[770, 570]
668.1086106589474
p: 
16
44
goal: 
[770, 570]
616.7959381271854
p: 
20
41
goal: 
[770, 570]
581.6705702051038
p: 
12
33
goal: 
[770, 570]
685.4950219731156
p: 
25
44
goal: 
[770, 570]
525.6677176788484
p: 
26
41
goal: 
[770, 570]
523.387548082565
p: 
26
39
goal: 
[770, 570]
538.4991191598917
p: 
14
41
goal: 
[770, 570]
640.2708746906757
p: 
32
42
goal: 
[770, 570]
465.54095448415046
p: 
32
39
goal: 
[770, 570]
481.42718070360945
p: 
20
41
goal: 
[770, 570]
581.6705849214098
p: 
26
41
goal: 
[770, 570]
523.387548082565
p: 
26
50
goal: 
[770, 570]
507.6125072375513
p: 
22
39
goal: 
[770, 570]
571.6557335428394
p: 
24
55
goal: 
[770, 570]
523.0462949257877
p: 
27
55
goal: 
[770, 570]
495.6869092232633
p: 
24
50
goal: 
[770, 570]
532.705622552933
p: 
26
50
goal: 
[770, 570]
507.6125072375513
p: 
31
36
goal: 
[770, 570]
498.31020345213557
p: 
29
34
goal: 
[770, 570]
521.5468373650949
p: 
27
33
goal: 
[770, 570]
548.8262201270929
p: 
25
36
goal: 
[770, 570]
554.5495511078674
p: 
31
28
goal: 
[770, 570]
537.9935272746128
p: 
26
39
goal: 
[770, 570]
538.4991191598917
p: 
32
23
goal: 
[770, 570]
559.9590270517577
p: 
29
23
goal: 
[770, 570]
582.8251684271947
p: 
27
24
goal: 
[770, 570]
593.557684166364
p: 
32
34
goal: 
[770, 570]
496.37573714465145
p: 
28
27
goal: 
[770, 570]
564.9161756566042
p: 
25
27
goal: 
[770, 570]
589.2195206722566
p: 
23
29
goal: 
[770, 570]
602.4247697798559
p: 
28
39
goal: 
[770, 570]
512.2897372152456
p: 
28
27
goal: 
[770, 570]
564.9161756566042
p: 
32
23
goal: 
[770, 570]
559.9590270517577
p: 
24
32
goal: 
[770, 570]
576.1132809350106
p: 
28
27
goal: 
[770, 570]
564.9161756566042
p: 
31
28
goal: 
[770, 570]
537.9935272746128
p: 
24
21
goal: 
[770, 570]
632.731416781892
p: 
22
23
goal: 
[770, 570]
644.2685859039623
p: 
27
33
goal: 
[770, 570]
548.8262201270929
p: 
14
50
goal: 
[770, 570]
627.6999520201701
p: 
17
50
goal: 
[770, 570]
600.4329328981931
p: 
18
38
goal: 
[770, 570]
611.6102926017621
p: 
13
45
goal: 
[770, 570]
641.0798772163915
p: 
23
20
goal: 
[770, 570]
649.5194919859532
p: 
21
22
goal: 
[770, 570]
652.4750675606693
p: 
21
25
goal: 
[770, 570]
640.0093328792975
p: 
32
26
goal: 
[770, 570]
534.8810605454524
p: 
15
55
goal: 
[770, 570]
616.67384424968
p: 
16
44
goal: 
[770, 570]
616.7959381271854
p: 
19
24
goal: 
[770, 570]
656.7436313286075
p: 
17
27
goal: 
[770, 570]
662.1504855681169
p: 
17
29
goal: 
[770, 570]
651.9396383973642
p: 
29
31
goal: 
[770, 570]
542.7595956222182
p: 
10
35
goal: 
[770, 570]
700.9726791532258
p: 
20
29
goal: 
[770, 570]
630.1493236941991
p: 
8
42
goal: 
[770, 570]
695.3682829211514
p: 
13
44
goal: 
[770, 570]
643.7537210528876
p: 
15
33
goal: 
[770, 570]
663.5852228867932
p: 
14
50
goal: 
[770, 570]
627.6999520201701
p: 
17
49
goal: 
[770, 570]
602.5279804822209
p: 
13
44
goal: 
[770, 570]
643.7537210528876
p: 
15
55
goal: 
[770, 570]
616.67384424968
p: 
16
44
goal: 
[770, 570]
616.7959381271854
p: 
25
21
goal: 
[770, 570]
624.435092759938
p: 
24
18
goal: 
[770, 570]
646.680695713374
p: 
22
16
goal: 
[770, 570]
674.0387456846942
p: 
15
25
goal: 
[770, 570]
691.5484820510673
p: 
20
19
goal: 
[770, 570]
681.7739538530499
p: 
30
17
goal: 
[770, 570]
608.0250517731481
p: 
29
15
goal: 
[770, 570]
631.6444256752885
p: 
27
13
goal: 
[770, 570]
658.8653736420342
p: 
20
22
goal: 
[770, 570]
666.7965068330542
p: 
36
16
goal: 
[770, 570]
572.6116817302681
p: 
24
15
goal: 
[770, 570]
663.5602883994475
p: 
42
15
goal: 
[770, 570]
541.0775488465922
p: 
41
13
goal: 
[770, 570]
566.6187846672555
p: 
38
11
goal: 
[770, 570]
593.0804031334526
p: 
46
19
goal: 
[770, 570]
483.58609645283923
p: 
47
17
goal: 
[770, 570]
491.67178372217023
p: 
47
14
goal: 
[770, 570]
514.1369380032437
p: 
36
13
goal: 
[770, 570]
592.4429950555107
p: 
51
21
goal: 
[770, 570]
434.7743343614027
p: 
53
19
goal: 
[770, 570]
444.8792820263412
p: 
53
16
goal: 
[770, 570]
468.51893613053016
p: 
42
15
goal: 
[770, 570]
541.0775488465922
p: 
51
27
goal: 
[770, 570]
394.08193411544426
p: 
53
27
goal: 
[770, 570]
377.3770135054033
p: 
56
25
goal: 
[770, 570]
378.1631806425326
p: 
49
15
goal: 
[770, 570]
492.7924359487424
p: 
51
21
goal: 
[770, 570]
434.7743468420505
p: 
61
27
goal: 
[770, 570]
334.032368997516
p: 
61
24
goal: 
[770, 570]
358.7880145633381
p: 
50
23
goal: 
[770, 570]
426.18868230227656
p: 
66
31
goal: 
[770, 570]
280.0792002048098
p: 
67
28
goal: 
[770, 570]
295.54640317552145
p: 
67
26
goal: 
[770, 570]
321.70790710132354
p: 
56
25
goal: 
[770, 570]
378.1631679104214
p: 
65
36
goal: 
[770, 570]
232.02843497725104
p: 
68
36
goal: 
[770, 570]
220.23084532009923
p: 
70
35
goal: 
[770, 570]
228.03987223556632
p: 
64
25
goal: 
[770, 570]
339.98082733409626
p: 
67
42
goal: 
[770, 570]
173.46880928955198
p: 
70
42
goal: 
[770, 570]
160.49533914638442
p: 
72
40
goal: 
[770, 570]
168.09622616751608
p: 
66
31
goal: 
[770, 570]
280.0792002048098
p: 
69
48
goal: 
[770, 570]
116.38523432525895
p: 
72
48
goal: 
[770, 570]
101.07296552139135
p: 
74
46
goal: 
[770, 570]
108.21442135212831
p: 
68
36
goal: 
[770, 570]
220.23084532009923
p: 
71
53
goal: 
[770, 570]
64.8033770953568
p: 
74
53
goal: 
[770, 570]
43.27319928397412
p: 
76
52
goal: 
[770, 570]
48.623537466535815
p: 
70
42
goal: 
[770, 570]
160.49533914638442
DONE
p: 
26
17
goal: 
[770, 570]
638.1915371180456
p: 
32
15
goal: 
[770, 570]
607.2851270675629
p: 
30
13
goal: 
[770, 570]
634.1797085319594
p: 
21
19
goal: 
[770, 570]
673.0391124366013
p: 
38
16
goal: 
[770, 570]
560.6511282261652
p: 
38
13
goal: 
[770, 570]
580.949231340024
p: 
36
11
goal: 
[770, 570]
608.1838906405686
p: 
26
17
goal: 
[770, 570]
638.1915371180456
p: 
40
21
goal: 
[770, 570]
505.16763914238936
p: 
43
20
goal: 
[770, 570]
501.9319153480891
p: 
43
17
goal: 
[770, 570]
516.2899104913099
p: 
33
13
goal: 
[770, 570]
619.6158289230274
p: 
45
25
goal: 
[770, 570]
446.0911334785156
p: 
47
23
goal: 
[770, 570]
443.5556962131797
p: 
48
20
goal: 
[770, 570]
458.64825600030787
p: 
38
16
goal: 
[770, 570]
560.6511282261652
p: 
52
26
goal: 
[770, 570]
385.67845843901847
p: 
53
24
goal: 
[770, 570]
401.6979535628743
p: 
43
20
goal: 
[770, 570]
501.9319153480891
p: 
47
23
goal: 
[770, 570]
443.55571617121825
p: 
59
25
goal: 
[770, 570]
364.2415727662186
p: 
59
22
goal: 
[770, 570]
388.6127575257732
p: 
57
20
goal: 
[770, 570]
415.62356651535816
p: 
48
26
goal: 
[770, 570]
422.96891747736856
p: 
62
30
goal: 
[770, 570]
306.40362005519836
p: 
64
28
goal: 
[770, 570]
311.564189214758
p: 
65
25
goal: 
[770, 570]
332.67660667603366
p: 
54
21
goal: 
[770, 570]
418.8931492042523
p: 
67
33
goal: 
[770, 570]
253.92993297697404
p: 
69
31
goal: 
[770, 570]
262.0542548018999
p: 
70
29
goal: 
[770, 570]
285.0806140966622
p: 
59
25
goal: 
[770, 570]
364.2415727662186
p: 
72
37
goal: 
[770, 570]
205.6150380436914
p: 
74
35
goal: 
[770, 570]
217.88182280171316
p: 
75
32
goal: 
[770, 570]
243.03920718038106
p: 
64
28
goal: 
[770, 570]
311.564189214758
p: 
69
42
goal: 
[770, 570]
164.93015107545156
p: 
72
43
goal: 
[770, 570]
147.6010283309869
p: 
74
42
goal: 
[770, 570]
150.24572505115796
p: 
71
31
goal: 
[770, 570]
264.51676129875574
p: 
69
48
goal: 
[770, 570]
113.61109654526787
p: 
72
49
goal: 
[770, 570]
92.16656710516736
p: 
74
48
goal: 
[770, 570]
90.99089970649835
p: 
72
37
goal: 
[770, 570]
205.6150380436914
p: 
69
54
goal: 
[770, 570]
76.2437249921179
p: 
72
55
goal: 
[770, 570]
49.02452592716717
p: 
75
54
goal: 
[770, 570]
34.42389202669313
p: 
72
43
goal: 
[770, 570]
147.6010283309869
DONE
p: 
39
17
goal: 
[770, 570]
541.0468269411938
p: 
42
22
goal: 
[770, 570]
485.4502963446738
p: 
44
21
goal: 
[770, 570]
482.42890148187246
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
34
14
goal: 
[770, 570]
599.9381141715285
p: 
47
26
goal: 
[770, 570]
426.45628372756534
p: 
49
24
goal: 
[770, 570]
424.1976767514246
p: 
50
21
goal: 
[770, 570]
439.5746714657652
p: 
39
17
goal: 
[770, 570]
541.0468269411938
p: 
55
25
goal: 
[770, 570]
382.9215980033812
p: 
44
21
goal: 
[770, 570]
482.42890148187246
p: 
49
27
goal: 
[770, 570]
403.41545773145197
p: 
47
20
goal: 
[770, 570]
472.54946550642507
p: 
54
17
goal: 
[770, 570]
451.4739707870683
p: 
44
23
goal: 
[770, 570]
462.1905381724247
p: 
52
23
goal: 
[770, 570]
413.51567948913504
p: 
45
27
goal: 
[770, 570]
430.44558822187656
p: 
42
16
goal: 
[770, 570]
530.4514328770648
p: 
40
24
goal: 
[770, 570]
489.9831455060755
p: 
51
19
goal: 
[770, 570]
456.075911860232
p: 
51
16
goal: 
[770, 570]
479.11371381521053
p: 
39
20
goal: 
[770, 570]
521.2445622577463
p: 
53
24
goal: 
[770, 570]
398.60776691325407
p: 
53
18
goal: 
[770, 570]
449.742335015954
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
55
25
goal: 
[770, 570]
382.9215980033812
p: 
53
23
goal: 
[770, 570]
410.2661800025644
p: 
49
27
goal: 
[770, 570]
403.41545773145197
p: 
55
17
goal: 
[770, 570]
449.398065622011
p: 
52
17
goal: 
[770, 570]
463.0931716751495
p: 
54
17
goal: 
[770, 570]
451.4739707870683
p: 
51
17
goal: 
[770, 570]
465.7379996101621
p: 
53
23
goal: 
[770, 570]
410.2661800025644
p: 
50
24
goal: 
[770, 570]
417.85457470363593
p: 
50
21
goal: 
[770, 570]
439.5746714657652
p: 
48
19
goal: 
[770, 570]
466.9324755787523
p: 
39
25
goal: 
[770, 570]
491.135716158703
p: 
45
21
goal: 
[770, 570]
475.90041840302837
p: 
54
17
goal: 
[770, 570]
451.4739707870683
p: 
44
23
goal: 
[770, 570]
462.1905381724247
p: 
52
23
goal: 
[770, 570]
413.51567948913504
p: 
52
23
goal: 
[770, 570]
413.51567948913504
p: 
51
23
goal: 
[770, 570]
420.37098803170824
p: 
53
24
goal: 
[770, 570]
398.60776691325407
p: 
53
18
goal: 
[770, 570]
449.742335015954
p: 
45
24
goal: 
[770, 570]
449.05610570170944
p: 
46
27
goal: 
[770, 570]
424.209145838265
p: 
51
23
goal: 
[770, 570]
420.37098803170824
p: 
44
25
goal: 
[770, 570]
450.3834663001941
p: 
47
26
goal: 
[770, 570]
426.45628372756534
p: 
50
25
goal: 
[770, 570]
415.84183322790403
p: 
55
26
goal: 
[770, 570]
374.428795046225
p: 
45
21
goal: 
[770, 570]
474.1341558307628
p: 
47
20
goal: 
[770, 570]
472.54946550642507
p: 
39
26
goal: 
[770, 570]
485.38677611354626
p: 
49
21
goal: 
[770, 570]
446.43178642511003
p: 
47
26
goal: 
[770, 570]
426.45628372756534
p: 
49
24
goal: 
[770, 570]
424.1976767514246
p: 
50
21
goal: 
[770, 570]
439.5746714657652
p: 
39
17
goal: 
[770, 570]
541.0468269411938
p: 
55
25
goal: 
[770, 570]
382.9215980033812
p: 
44
21
goal: 
[770, 570]
482.42890148187246
p: 
49
27
goal: 
[770, 570]
403.41545773145197
p: 
47
20
goal: 
[770, 570]
472.54946550642507
p: 
54
17
goal: 
[770, 570]
451.4739707870683
p: 
44
23
goal: 
[770, 570]
462.1905381724247
p: 
52
23
goal: 
[770, 570]
413.51567948913504
p: 
46
25
goal: 
[770, 570]
435.28280714859426
p: 
55
22
goal: 
[770, 570]
405.8252029315262
p: 
41
20
goal: 
[770, 570]
506.8027896089125
p: 
39
23
goal: 
[770, 570]
501.802207265891
p: 
40
25
goal: 
[770, 570]
482.9928961139529
p: 
51
26
goal: 
[770, 570]
398.3681880741384
p: 
51
19
goal: 
[770, 570]
456.075911860232
p: 
51
16
goal: 
[770, 570]
479.11371381521053
p: 
39
20
goal: 
[770, 570]
521.2445622577463
p: 
53
24
goal: 
[770, 570]
398.60776691325407
p: 
53
18
goal: 
[770, 570]
449.742335015954
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
45
27
goal: 
[770, 570]
430.44558822187656
p: 
46
25
goal: 
[770, 570]
442.8659847318036
p: 
40
24
goal: 
[770, 570]
489.9831455060755
p: 
51
26
goal: 
[770, 570]
398.5827282469302
p: 
51
23
goal: 
[770, 570]
420.37517986315385
p: 
50
21
goal: 
[770, 570]
447.7343657825813
p: 
40
27
goal: 
[770, 570]
471.95903100165737
p: 
46
22
goal: 
[770, 570]
456.5897887485355
p: 
55
19
goal: 
[770, 570]
432.72167365247935
p: 
46
25
goal: 
[770, 570]
442.86600603558645
p: 
53
24
goal: 
[770, 570]
394.36459175290196
p: 
54
17
goal: 
[770, 570]
459.8836222102737
p: 
48
26
goal: 
[770, 570]
415.9568423131586
p: 
48
18
goal: 
[770, 570]
475.0934555563137
p: 
45
21
goal: 
[770, 570]
475.90044131159874
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
43
16
goal: 
[770, 570]
524.3409072489952
p: 
48
26
goal: 
[770, 570]
419.75681239930753
p: 
50
24
goal: 
[770, 570]
417.8545982855668
p: 
51
22
goal: 
[770, 570]
433.54084501333455
p: 
40
17
goal: 
[770, 570]
534.3781832253112
p: 
45
21
goal: 
[770, 570]
475.90044131159874
p: 
48
20
goal: 
[770, 570]
466.3274384764098
p: 
55
17
goal: 
[770, 570]
446.2597314207017
p: 
45
24
goal: 
[770, 570]
455.45213237345627
p: 
53
23
goal: 
[770, 570]
407.6047739081773
p: 
51
19
goal: 
[770, 570]
456.075911860232
p: 
51
16
goal: 
[770, 570]
479.11371381521053
p: 
39
20
goal: 
[770, 570]
521.2445622577463
p: 
53
24
goal: 
[770, 570]
398.60776691325407
p: 
53
18
goal: 
[770, 570]
449.742335015954
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
39
22
goal: 
[770, 570]
509.65941665434366
p: 
42
22
goal: 
[770, 570]
485.4502963446738
p: 
45
21
goal: 
[770, 570]
474.13411065517016
p: 
42
10
goal: 
[770, 570]
578.18287597451
p: 
47
26
goal: 
[770, 570]
418.2328272759646
p: 
50
25
goal: 
[770, 570]
415.8417867618466
p: 
50
22
goal: 
[770, 570]
431.1364135572788
p: 
40
18
goal: 
[770, 570]
532.8057489279569
p: 
55
26
goal: 
[770, 570]
374.4287447789518
p: 
45
21
goal: 
[770, 570]
474.13411065517016
p: 
47
21
goal: 
[770, 570]
464.15674047907214
p: 
54
18
goal: 
[770, 570]
442.93466827929205
p: 
45
24
goal: 
[770, 570]
453.98274433170207
p: 
53
24
goal: 
[770, 570]
405.05284724259076
p: 
45
27
goal: 
[770, 570]
430.44558822187656
p: 
42
16
goal: 
[770, 570]
530.4514328770648
p: 
40
24
goal: 
[770, 570]
489.9831455060755
p: 
44
18
goal: 
[770, 570]
504.07748591596726
p: 
42
22
goal: 
[770, 570]
485.4502963446738
p: 
44
21
goal: 
[770, 570]
482.42890148187246
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
34
14
goal: 
[770, 570]
599.9381141715285
p: 
47
26
goal: 
[770, 570]
426.45628372756534
p: 
49
24
goal: 
[770, 570]
424.1976767514246
p: 
50
21
goal: 
[770, 570]
439.5746714657652
p: 
39
17
goal: 
[770, 570]
541.0468269411938
p: 
55
25
goal: 
[770, 570]
382.9215980033812
p: 
44
21
goal: 
[770, 570]
482.42890148187246
p: 
49
27
goal: 
[770, 570]
403.41545773145197
p: 
47
20
goal: 
[770, 570]
472.54946550642507
p: 
54
17
goal: 
[770, 570]
451.4739707870683
p: 
44
23
goal: 
[770, 570]
462.1905381724247
p: 
52
23
goal: 
[770, 570]
413.51567948913504
p: 
45
27
goal: 
[770, 570]
430.44558822187656
p: 
42
16
goal: 
[770, 570]
530.4514328770648
p: 
40
24
goal: 
[770, 570]
489.9831455060755
p: 
51
19
goal: 
[770, 570]
456.075911860232
p: 
51
16
goal: 
[770, 570]
479.11371381521053
p: 
39
20
goal: 
[770, 570]
521.2445622577463
p: 
53
24
goal: 
[770, 570]
398.60776691325407
p: 
53
18
goal: 
[770, 570]
449.742335015954
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
44
22
goal: 
[770, 570]
474.17971443472885
p: 
42
22
goal: 
[770, 570]
494.23070998193714
p: 
45
24
goal: 
[770, 570]
449.05610570170944
p: 
42
15
goal: 
[770, 570]
545.4480669700899
p: 
39
15
goal: 
[770, 570]
562.2615091950834
p: 
37
17
goal: 
[770, 570]
564.5687315050852
p: 
43
26
goal: 
[770, 570]
452.5042483969619
p: 
39
17
goal: 
[770, 570]
541.0468269411938
p: 
40
15
goal: 
[770, 570]
554.9954800565229
p: 
29
10
goal: 
[770, 570]
659.0294839099944
p: 
42
22
goal: 
[770, 570]
485.4502963446738
p: 
44
21
goal: 
[770, 570]
482.42890148187246
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
34
14
goal: 
[770, 570]
599.9381141715285
p: 
47
26
goal: 
[770, 570]
426.45628372756534
p: 
49
24
goal: 
[770, 570]
424.1976767514246
p: 
50
21
goal: 
[770, 570]
439.5746714657652
p: 
39
17
goal: 
[770, 570]
541.0468269411938
p: 
55
25
goal: 
[770, 570]
382.9215980033812
p: 
44
21
goal: 
[770, 570]
482.42890148187246
p: 
49
27
goal: 
[770, 570]
403.41545773145197
p: 
47
20
goal: 
[770, 570]
472.54946550642507
p: 
54
17
goal: 
[770, 570]
451.4739707870683
p: 
44
23
goal: 
[770, 570]
462.1905381724247
p: 
52
23
goal: 
[770, 570]
413.51567948913504
p: 
45
27
goal: 
[770, 570]
430.44558822187656
p: 
42
16
goal: 
[770, 570]
530.4514328770648
p: 
40
24
goal: 
[770, 570]
489.9831455060755
p: 
51
19
goal: 
[770, 570]
456.075911860232
p: 
51
16
goal: 
[770, 570]
479.11371381521053
p: 
39
20
goal: 
[770, 570]
521.2445622577463
p: 
53
24
goal: 
[770, 570]
398.60776691325407
p: 
53
18
goal: 
[770, 570]
449.742335015954
p: 
45
18
goal: 
[770, 570]
497.01400791142026
p: 
34
17
goal: 
[770, 570]
580.4926541449076
p: 
38
20
goal: 
[770, 570]
530.5461010929288
p: 
39
9
goal: 
[770, 570]
602.4943880984406
p: 
37
9
goal: 
[770, 570]
618.5684405292021
p: 
34
11
goal: 
[770, 570]
619.8578414571634
p: 
41
20
goal: 
[770, 570]
506.8027896089125
p: 
32
13
goal: 
[770, 570]
622.348564276675
p: 
31
15
goal: 
[770, 570]
617.4835048572022
p: 
42
18
goal: 
[770, 570]
513.2152206856059
p: 
44
6
goal: 
[770, 570]
597.7473036186304
p: 
43
4
goal: 
[770, 570]
624.9102702814275
p: 
40
3
goal: 
[770, 570]
645.4083837002529
p: 
36
14
goal: 
[770, 570]
585.3940505548425
p: 
50
8
goal: 
[770, 570]
551.0608952914095
p: 
50
6
goal: 
[770, 570]
571.3447279828825
p: 
49
3
goal: 
[770, 570]
598.577657395434
p: 
38
7
goal: 
[770, 570]
628.7835864438005
p: 
46
4
goal: 
[770, 570]
610.0387721324453
p: 
56
8
goal: 
[770, 570]
528.2026383691242
p: 
56
5
goal: 
[770, 570]
550.2429634674841
p: 
55
3
goal: 
[770, 570]
577.602887808498
p: 
44
6
goal: 
[770, 570]
597.7473036186304
p: 
61
10
goal: 
[770, 570]
488.1109819789499
p: 
52
3
goal: 
[770, 570]
585.831073918818
p: 
66
12
goal: 
[770, 570]
451.88242366329547
p: 
67
10
goal: 
[770, 570]
476.42304764185553
p: 
66
7
goal: 
[770, 570]
503.3840300466001
p: 
68
18
goal: 
[770, 570]
394.04398674713696
p: 
70
17
goal: 
[770, 570]
399.48883923145945
p: 
72
15
goal: 
[770, 570]
420.5165831395546
p: 
62
8
goal: 
[770, 570]
505.9682265181981
p: 
72
23
goal: 
[770, 570]
341.8497669670645
p: 
74
22
goal: 
[770, 570]
349.54954565028044
p: 
76
19
goal: 
[770, 570]
372.0547623164218
p: 
66
12
goal: 
[770, 570]
451.88242366329547
p: 
75
27
goal: 
[770, 570]
292.663300053882
p: 
78
26
goal: 
[770, 570]
303.2793936984863
p: 
79
24
goal: 
[770, 570]
327.4373638142267
p: 
70
17
goal: 
[770, 570]
399.48883923145945
p: 
72
32
goal: 
[770, 570]
252.76857295350814
p: 
74
33
goal: 
[770, 570]
235.34658542336078
p: 
77
33
goal: 
[770, 570]
236.24108959182323
p: 
77
21
goal: 
[770, 570]
350.878453245845
p: 
70
38
goal: 
[770, 570]
199.5622334726781
p: 
73
39
goal: 
[770, 570]
179.78907009067063
p: 
75
39
goal: 
[770, 570]
178.16569012317103
p: 
75
27
goal: 
[770, 570]
292.663300053882
p: 
69
43
goal: 
[770, 570]
151.51932208758234
p: 
71
45
goal: 
[770, 570]
128.29688444902723
p: 
74
45
goal: 
[770, 570]
121.9674556766103
p: 
74
33
goal: 
[770, 570]
235.34658542336078
p: 
68
49
goal: 
[770, 570]
115.28664833701899
p: 
70
51
goal: 
[770, 570]
88.29472111180903
p: 
73
50
goal: 
[770, 570]
72.17335888686432
p: 
73
39
goal: 
[770, 570]
179.78907009067063
p: 
74
56
goal: 
[770, 570]
25.47566360062295
p: 
77
55
goal: 
[770, 570]
15.25428420073609
p: 
78
53
goal: 
[770, 570]
41.19385016147486
p: 
69
46
goal: 
[770, 570]
131.85319721032562
DONE
                                                                                                                                         readme.txt                                                                                          0000600 0000000 0000000 00000000153 11753164032 011543  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   CarSim.jar must be in jython classpath
use "jython -Dpython.path=CarSim.jar Car.py" to start example car
                                                                                                                                                                                                                                                                                                                                                                                                                     src/                                                                                                0000700 0000000 0000000 00000000000 11762166564 010347  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/                                                                                            0000700 0000000 0000000 00000000000 11762166564 011125  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/controller/                                                                                 0000700 0000000 0000000 00000000000 11762166564 013310  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/controller/D.java                                                                           0000600 0000000 0000000 00000000711 11743745010 014323  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.controller;

/**
 * Differencial Element. Output = dInput * dT
 */
public class D extends ElementHelper
{
	private float kd = 0.f;
	private float last = 0.f;
	
	public D(float kd) 
	{
		super(0);
		this.kd = kd;
	}
	
	@Override
	public float update(float dt) 
	{
		value = dt*kd*(input - last);
		last = input;
		return value;
	}
	
	@Override
	public void value(float s) 
	{
		super.value(s);
		last = s;
	}
}
                                                       src/com/controller/D.java~                                                                          0000600 0000000 0000000 00000000726 11730331040 014515  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.controller;

/**
 * Differencial Element. Output = dInput * dT
 */
public class D extends ElementHelper
{
	private float kd = 0.f;
	private float last = 0.f;
	
	public D(float kd) 
	{
		super(0);
		this.kd = kd;
	}
	
	@Override
	public float update(float dt) 
	{
		value = dt*kd*(input - last);
		last = input;
		return value;
	}
	
	@Override
	public void value(float s) 
	{
		super.value(s);
		last = s;
	}
}
                                          src/com/controller/Element.java                                                                     0000600 0000000 0000000 00000001236 11743745010 015534  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.controller;

public interface Element 
{
	/**
	 * Sets input value of the Element
	 * @param in Input Value
	 */
	public void input(float in);
	
	/**
	 * Returns current input value
	 * @return current input value
	 */
	public float input();

	/**
	 * Updates the Element's value after dt Time
	 * @param time difference 
	 * @return current value
	 */
	public float update(float dt);
	
	/**
	 * Sets the current value of the Element
	 * but leaves the input value unchanged.
	 * @param s value 
	 */
	public void value(float s);

	/**
	 * Returns current value
	 * @return current value
	 */
	public float value();
}
                                                                                                                                                                                                                                                                                                                                                                  src/com/controller/Element.java~                                                                    0000600 0000000 0000000 00000001253 11724424316 015733  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.controller;

public interface Element 
{
	/**
	 * Sets input value of the Element
	 * @param in Input Value
	 */
	public void input(float in);
	
	/**
	 * Returns current input value
	 * @return current input value
	 */
	public float input();

	/**
	 * Updates the Element's value after dt Time
	 * @param time difference 
	 * @return current value
	 */
	public float update(float dt);
	
	/**
	 * Sets the current value of the Element
	 * but leaves the input value unchanged.
	 * @param s value 
	 */
	public void value(float s);

	/**
	 * Returns current value
	 * @return current value
	 */
	public float value();
}
                                                                                                                                                                                                                                                                                                                                                     src/com/controller/ElementHelper.java                                                               0000600 0000000 0000000 00000001000 11743745010 016661  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.controller;

abstract class ElementHelper implements Element
{
	protected float value = 0.f;
	protected float input = 0.f;
	
	public ElementHelper(float start)
	{
		value = start;
	}
	
	public ElementHelper()
	{
	}

	@Override
	public void value(float s) 
	{
		value = s;
	}

	@Override
	public float value() 
	{
		return value;
	}

	@Override
	public void input(float in) 
	{
		input = in;
	}	
	
	@Override
	public float input() 
	{
		return input;
	}	
}
src/com/controller/ElementHelper.java~                                                              0000600 0000000 0000000 00000001015 11724424244 017067  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.controller;

abstract class ElementHelper implements Element
{
	protected float value = 0.f;
	protected float input = 0.f;
	
	public ElementHelper(float start)
	{
		value = start;
	}
	
	public ElementHelper()
	{
	}

	@Override
	public void value(float s) 
	{
		value = s;
	}

	@Override
	public float value() 
	{
		return value;
	}

	@Override
	public void input(float in) 
	{
		input = in;
	}	
	
	@Override
	public float input() 
	{
		return input;
	}	
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   src/com/controller/I.java                                                                           0000600 0000000 0000000 00000000505 11743744776 014353  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.controller;

/**
 * Integral Element. output = Integral of input
 */
public class I extends ElementHelper
{
	private float ki = 0.f;
	
	public I(float ki) 
	{
		super(0);
		this.ki = ki;
	}
	
	@Override
	public float update(float dt) 
	{
		value += input * ki * dt;
		return value;
	}
}
                                                                                                                                                                                           src/com/controller/I.java~                                                                          0000600 0000000 0000000 00000000522 11724424464 014534  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.controller;

/**
 * Integral Element. output = Integral of input
 */
public class I extends ElementHelper
{
	private float ki = 0.f;
	
	public I(float ki) 
	{
		super(0);
		this.ki = ki;
	}
	
	@Override
	public float update(float dt) 
	{
		value += input * ki * dt;
		return value;
	}
}
                                                                                                                                                                              src/com/controller/Link.java                                                                        0000600 0000000 0000000 00000000371 11743745032 015043  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.controller;

/**
 * Direkt link. input = output
 */
public class Link extends ElementHelper
{
	public Link() 
	{
		super(0);
	}
	
	@Override
	public float update(float dt) 
	{
		value = input;
		return value;
	}
}
                                                                                                                                                                                                                                                                       src/com/controller/Link.java~                                                                       0000600 0000000 0000000 00000000406 11724627402 015237  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.controller;

/**
 * Direkt link. input = output
 */
public class Link extends ElementHelper
{
	public Link() 
	{
		super(0);
	}
	
	@Override
	public float update(float dt) 
	{
		value = input;
		return value;
	}
}
                                                                                                                                                                                                                                                          src/com/controller/P.java                                                                           0000600 0000000 0000000 00000000500 11743745070 014341  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.controller;

/**
 * Proportional Element.
 * output = input * kp
 */
public class P extends ElementHelper
{
	private float kp = 0.f;
	
	public P(float kp) 
	{
		super(0);
		this.kp = kp;
	}
	
	@Override
	public float update(float dt) 
	{
		value = input * kp;
		return value;
	}
}
                                                                                                                                                                                                src/com/controller/P.java~                                                                          0000600 0000000 0000000 00000000515 11724424426 014543  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.controller;

/**
 * Proportional Element.
 * output = input * kp
 */
public class P extends ElementHelper
{
	private float kp = 0.f;
	
	public P(float kp) 
	{
		super(0);
		this.kp = kp;
	}
	
	@Override
	public float update(float dt) 
	{
		value = input * kp;
		return value;
	}
}
                                                                                                                                                                                   src/com/controller/PT1.java                                                                         0000600 0000000 0000000 00000001541 11743745060 014553  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.controller;

/**
 * First order lag Element. ouput = input * 1-e^(-t/T)
 */
public class PT1 implements Element
{
	private float t = 0.f;
	private float time = 0.f;
	private float offset = 0.f;
	private float relative = 0.f;
	private float value = 0.f;
	
	public PT1(float t)
	{
		this.t = t;
	}
	
	@Override
	public float update(float dt) 
	{
		time += dt;
		value = offset + relative * (1.f - (float)Math.exp(-time/t));
		return value;
	}
	
	@Override
	public void value(float s) 
	{
		time = 0.0f;
		relative = relative - s;
		offset = s;
		value = s;
	}
	
	@Override
	public void input(float in) 
	{
		time = 0.0f;
		relative = in - value;
		offset = value;
	}

	@Override
	public float value() 
	{
		return value;
	}
	
	@Override
	public float input() 
	{
		return offset + relative;
	}
}
                                                                                                                                                               src/com/controller/PT1.java~                                                                        0000600 0000000 0000000 00000001556 11726640544 014761  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.controller;

/**
 * First order lag Element. ouput = input * 1-e^(-t/T)
 */
public class PT1 implements Element
{
	private float t = 0.f;
	private float time = 0.f;
	private float offset = 0.f;
	private float relative = 0.f;
	private float value = 0.f;
	
	public PT1(float t)
	{
		this.t = t;
	}
	
	@Override
	public float update(float dt) 
	{
		time += dt;
		value = offset + relative * (1.f - (float)Math.exp(-time/t));
		return value;
	}
	
	@Override
	public void value(float s) 
	{
		time = 0.0f;
		relative = relative - s;
		offset = s;
		value = s;
	}
	
	@Override
	public void input(float in) 
	{
		time = 0.0f;
		relative = in - value;
		offset = value;
	}

	@Override
	public float value() 
	{
		return value;
	}
	
	@Override
	public float input() 
	{
		return offset + relative;
	}
}
                                                                                                                                                  src/com/controller/PT2.java                                                                         0000600 0000000 0000000 00000001336 11743745046 014562  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.controller;

/**
 * Second order lag, build out of 2 first order lags in series.
 */
public class PT2 implements Element
{
	private PT1 pt1;
	private PT1 pt2;
	
	public PT2(float T1, float T2)
	{
		pt1 = new PT1(T1);
		pt2 = new PT1(T2);
	}
	
	public PT2(float T1)
	{
		this(T1,T1);
	}
	
	@Override
	public float update(float dt) 
	{
		pt2.input(pt1.update(dt));
		return pt2.update(dt);
	}
	
	@Override
	public void input(float in) 
	{
		pt1.input(in);
	}
	
	@Override
	public void value(float s)
	{
		pt1.value(s);
		pt2.value(s);
	}

	@Override
	public float value() 
	{
		return pt2.value();
	}
	
	@Override
	public float input() 
	{
		return pt1.input();
	}
}
                                                                                                                                                                                                                                                                                                  src/com/controller/PT2.java~                                                                        0000600 0000000 0000000 00000001353 11724424652 014753  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.controller;

/**
 * Second order lag, build out of 2 first order lags in series.
 */
public class PT2 implements Element
{
	private PT1 pt1;
	private PT1 pt2;
	
	public PT2(float T1, float T2)
	{
		pt1 = new PT1(T1);
		pt2 = new PT1(T2);
	}
	
	public PT2(float T1)
	{
		this(T1,T1);
	}
	
	@Override
	public float update(float dt) 
	{
		pt2.input(pt1.update(dt));
		return pt2.update(dt);
	}
	
	@Override
	public void input(float in) 
	{
		pt1.input(in);
	}
	
	@Override
	public void value(float s)
	{
		pt1.value(s);
		pt2.value(s);
	}

	@Override
	public float value() 
	{
		return pt2.value();
	}
	
	@Override
	public float input() 
	{
		return pt1.input();
	}
}
                                                                                                                                                                                                                                                                                     src/com/lib/                                                                                        0000700 0000000 0000000 00000000000 11762166564 011673  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/lib/controller/                                                                             0000700 0000000 0000000 00000000000 11762166564 014056  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/lib/controller/D.class                                                                      0000600 0000000 0000000 00000000774 11757604526 015301  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 "
  	 
 	 
 	 
 	 
 
  
  
  
     ! kd F last <init> (F)V Code update (F)F value input ()F                   com/lib/controller/D  com/lib/controller/ElementHelper ! 
                       !     *� *� *� *#� �            -     !*#*� j*� *� fj� **� � *� �                 *#� *#� �    A            *� �    A            *#� �    A            *� 	�          src/com/lib/controller/Element.class                                                                0000600 0000000 0000000 00000000243 11757604526 016476  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2  	 
 input (F)V ()F update (F)F value com/lib/controller/Element java/lang/Object                                                                                                                                                                                                                                                                                                                                                                                          src/com/lib/controller/ElementHelper.class                                                          0000600 0000000 0000000 00000000660 11757604526 017641  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 
  	  	      value F input <init> (F)V Code ()V ()F 
    	   com/lib/controller/ElementHelper java/lang/Object com/lib/controller/Element             	      
            *� *� *� *#� �      
           *� *� *� �                 *#� �                 *� �      	           *#� �      	           *� �                                                                                      src/com/lib/controller/I.class                                                                      0000600 0000000 0000000 00000000721 11757604526 015276  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 
 
 	 	 	 	 	 	 
 
 
 
 
 
 
 
    ki F <init> (F)V Code update (F)F input ()F value                 com/lib/controller/I  com/lib/controller/ElementHelper ! 	 
                      *� *� *#� �            %     *Y� *� *� j#jb� *� �    A            *� �    A            *#� �    A            *� �    A            *#� �                                                     src/com/lib/controller/Link.class                                                                   0000600 0000000 0000000 00000000655 11757604526 016011  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 
 	 	  	  
 	 
 	 
 	 
 	    <init> ()V Code update (F)F input ()F (F)V value 
              com/lib/controller/Link  com/lib/controller/ElementHelper F !  	       
           *� �                 **� � *� �    A            *� �    A            *#� �    A            *� �    A            *#� �                                                                                         src/com/lib/controller/P.class                                                                      0000600 0000000 0000000 00000000712 11757604526 015305  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 
 
 	 	 	 	 	 	 
 
 
 
 
 
 
 
    kp F <init> (F)V Code update (F)F input ()F value                 com/lib/controller/P  com/lib/controller/ElementHelper ! 	 
                      *� *� *#� �                 **� *� j� *� �    A            *� �    A            *#� �    A            *� �    A            *#� �                                                            src/com/lib/controller/PT1.class                                                                    0000600 0000000 0000000 00000001217 11757604526 015513  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 '
 	 	  	  	  	  	  
     ! " t F time offset relative value <init> (F)V Code update (F)F input ()F  #           $ % & com/lib/controller/PT1 java/lang/Object com/lib/controller/Element ()V java/lang/Math exp (D)D !  	  
                                   /     #*� *� *� *� *� *� *#� �            :     .*Y� #b� **� *� *� v*� n�� �fjb� *� �            &     *� **� #f� *#� *#� �            $     *� *#*� f� **� � �                 *� �                 
*� *� b�                                                                                                                                                                                                                                                                                                                                                                                       src/com/lib/controller/PT2.class                                                                    0000600 0000000 0000000 00000001212 11757604526 015507  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 *
   
  	  	  
   
  !
  "
  #
  $
  % & ' ( pt1 Lcom/lib/controller/PT1; pt2 <init> (FF)V Code (F)V update (F)F input value ()F  ) com/lib/controller/PT1                   com/lib/controller/PT2 java/lang/Object com/lib/controller/Element ()V !                        )     *� *� Y#� � *� Y$� � �                 *##� �            $     *� *� #� � *� #� �                 	*� #� �                 *� #� 	*� #� 	�                 *� � 
�                 *� � �                                                                                                                                                                                                                                                                                                                                                                                            src/com/lib/udacity/                                                                                0000700 0000000 0000000 00000000000 11762166564 013335  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/lib/udacity/simulator/                                                                      0000700 0000000 0000000 00000000000 11762166564 015354  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/lib/udacity/simulator/abstracts/                                                            0000700 0000000 0000000 00000000000 11762166564 017342  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/lib/udacity/simulator/abstracts/Background.class                                            0000600 0000000 0000000 00000000241 11757604526 022446  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 	   getColorAtPixel (FF)I 
getColorAt (II)I .com/lib/udacity/simulator/abstracts/Background java/lang/Object                                                                                                                                                                                                                                                                                                                                                                                src/com/lib/udacity/simulator/abstracts/Car.class                                                   0000600 0000000 0000000 00000000504 11757604526 021076  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2     getX ()F getY getAngle getSteer getSpeed getController 5()Lcom/lib/udacity/simulator/abstracts/CarController; 'com/lib/udacity/simulator/abstracts/Car java/lang/Object 4com/lib/udacity/simulator/abstracts/SimulationObject                        	    
                                                                                                                                                                                                 src/com/lib/udacity/simulator/abstracts/CarController.class                                         0000600 0000000 0000000 00000000275 11757604526 023147  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2  	 
 getSpeed ()F getGyro setSpeed (F)V setSteer 1com/lib/udacity/simulator/abstracts/CarController java/lang/Object                                                                                                                                                                                                                                                                                                                                                            src/com/lib/udacity/simulator/abstracts/Configurable.class                                          0000600 0000000 0000000 00000000231 11757604526 022766  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2    loadProperties (Ljava/util/Properties;)V 0com/lib/udacity/simulator/abstracts/Configurable java/lang/Object                                                                                                                                                                                                                                                                                                                                                                                    src/com/lib/udacity/simulator/abstracts/SimulationListener.class                                    0000600 0000000 0000000 00000000561 11757604526 024226  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2    init f(Lcom/lib/udacity/simulator/abstracts/CarController;Lcom/lib/udacity/simulator/abstracts/Background;)V onUpdate (F)V onGPS ([F)V onCamera ([[I)V onPaint (Ljava/awt/Graphics2D;)V 	onScanner 6com/lib/udacity/simulator/abstracts/SimulationListener java/lang/Object                    	 
        
                                                                                                                                                   src/com/lib/udacity/simulator/abstracts/SimulationObject.class                                      0000600 0000000 0000000 00000000372 11757604526 023647  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2  
   init ()V update (F)V onPaint (Ljava/awt/Graphics2D;)V 4com/lib/udacity/simulator/abstracts/SimulationObject java/lang/Object 0com/lib/udacity/simulator/abstracts/Configurable                 	                                                                                                                                                                                                                                                                          src/com/lib/udacity/simulator/BicycleModel.class                                                    0000600 0000000 0000000 00000000776 11757604526 020751  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 !
  
  
  ?PbM���
  
  @!�TD-   <init> ()V Code getPos (FFFFFFF)[F StackMapTable             &com/lib/udacity/simulator/BicycleModel java/lang/Object java/lang/Math tan (D)D abs (F)F sin cos ! 
                   *� �     	       �     �%�� �8j8nj8		� � �� Rn8
"$�� �
jf8#$�� �
jb8$	b�� �
jbC$	b�� �
jfD$	b� s�E� "��$�� kc�C#��$�� kc�D�Y"QY#QY$Q�       	 � u    src/com/lib/udacity/simulator/DefaultCar$1.class                                                    0000600 0000000 0000000 00000000302 11757604526 020536  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 
   EnclosingMethod 	 &com/lib/udacity/simulator/DefaultCar$1   InnerClasses java/lang/Object $com/lib/udacity/simulator/DefaultCar                     
                                                                                                                                                                                                                                                                                                                                   src/com/lib/udacity/simulator/DefaultCar$DefaultCarController.class                                 0000600 0000000 0000000 00000002455 11757604526 024467  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 C
  $	  %
  &
 ' (
 ' )��  
 ' *
 ' +
 ' ,
 ' -
 ' .
 ' /
 ' 0 1 3 4 this$0 &Lcom/lib/udacity/simulator/DefaultCar; <init> )(Lcom/lib/udacity/simulator/DefaultCar;)V Code getSpeed ()F getGyro setSpeed (F)V StackMapTable setSteer getPos ()[F getAngle 5   InnerClasses Q(Lcom/lib/udacity/simulator/DefaultCar;Lcom/lib/udacity/simulator/DefaultCar$1;)V      6 7 8 9 : 9 ; 9 < = > 9 ? = @ 9 A 9 B 9 9com/lib/udacity/simulator/DefaultCar$DefaultCarController DefaultCarController java/lang/Object 1com/lib/udacity/simulator/abstracts/CarController &com/lib/udacity/simulator/DefaultCar$1 ()V $com/lib/udacity/simulator/DefaultCar 
access$000 )(Lcom/lib/udacity/simulator/DefaultCar;)F 
access$100 
access$300 
access$202 *(Lcom/lib/udacity/simulator/DefaultCar;F)F 
access$500 
access$402 
access$600 
access$700 
access$800 !                       
*+� *� �                 *� � �                 *� � �            =     '#�� D� #�� D*� #*� � j� W�        	        =     '#�� D� #�� D*� #*� � 	j� 
W�        	        $     �Y*� � QY*� � Q�                 *� � �       #          *+� �      "       '    ' 2                                                                                                                                                                                                                    src/com/lib/udacity/simulator/DefaultCar.class                                                      0000600 0000000 0000000 00000012303 11757604526 020415  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2>	 ` �	 ` �	 ` �	 ` �	 ` �	 ` �	 ` �	 ` �	 ` �
 a �	 ` �	 ` �	 ` �	 ` �?   	 ` �B�  	 ` � �
  �	 ` � �
  �	 ` �
 a � �
 � � � �
  �
 � �	 ` �
 � � �
 " �	 � � �
 � �	 ` �	 ` � � �	 ` �
  � � � � �
 � �
 � �?PbM���
 � �
 � �@!�TD- � �
 � �
 � � � � � � � � �	 ` � �	 ` � �	 ` � � � r � � �
 K � �
 M � �
 Q � �	 � �
 Q �?�!�TD-
 Q �	 � �	 � �
 Q �@6�     BH  
 Q �
 Q � � �    InnerClasses DefaultCarController carImage Ljava/awt/Image; speedSensorError F gyroSensorError 
steerError 
speedError maxSpeed maxSteer 
randomTime 	carLength r Lcom/lib/util/Random; 
controller 3Lcom/lib/udacity/simulator/abstracts/CarController; x y startX startY startA angle speed Lcom/lib/controller/Element; steer desiredSteer desiredSpeed retSpeed retGyro time <init> ()V Code StackMapTable  � getX ()F getY getAngle getSteer getSpeed getController 5()Lcom/lib/udacity/simulator/abstracts/CarController; update (F)V loadProperties (Ljava/util/Properties;)V onPaint (Ljava/awt/Graphics2D;)V init 
access$000 )(Lcom/lib/udacity/simulator/DefaultCar;)F 
access$100 
access$202 *(Lcom/lib/udacity/simulator/DefaultCar;F)F 
access$300 
access$402 
access$500 
access$600 
access$700 
access$800 | k x k w k p k � k o k � k � k � k � � j k l k m k n k q k r k 9com/lib/udacity/simulator/DefaultCar$DefaultCarController � u v com/lib/util/Random s t /img/car.png	
 java/io/File img/car.png � h i java/lang/Exception � Couldn't load img/car.png � k  ~ � } ~ � � ! carSpeedSensorError 0"#$%&' carGyroSensorError carSteerError carSpeedError carMaxSpeed carMaxSteer 	carStartX 200 y k 	carStartY z k carStartAngle { k errorUpdateTime 0.5 100 	carSpeedT com/lib/controller/PT1 � � com/lib/controller/Link 	carSteerT() java/awt/Graphics2D*+,-./01256789:;< � � $com/lib/udacity/simulator/DefaultCar java/lang/Object 'com/lib/udacity/simulator/abstracts/Car 0com/lib/udacity/simulator/abstracts/Configurable &com/lib/udacity/simulator/DefaultCar$1 Q(Lcom/lib/udacity/simulator/DefaultCar;Lcom/lib/udacity/simulator/DefaultCar$1;)V getClass ()Ljava/lang/Class; java/lang/Class getResource "(Ljava/lang/String;)Ljava/net/URL; (Ljava/lang/String;)V javax/imageio/ImageIO read .(Ljava/io/File;)Ljava/awt/image/BufferedImage; .(Ljava/net/URL;)Ljava/awt/image/BufferedImage; printStackTrace java/lang/System err Ljava/io/PrintStream; java/io/PrintStream println com/lib/controller/Element value nextGaussian (FF)D input (F)F java/lang/Math tan (D)D abs sin cos java/util/Properties getProperty 8(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String; java/lang/Float 
parseFloat (Ljava/lang/String;)F create ()Ljava/awt/Graphics; java/awt/Color BLUE Ljava/awt/Color; setColor (Ljava/awt/Color;)V rotate (DDD)V java/awt/RenderingHints KEY_ANTIALIASING= Key Ljava/awt/RenderingHints$Key; VALUE_ANTIALIAS_ON Ljava/lang/Object; setRenderingHint 2(Ljava/awt/RenderingHints$Key;Ljava/lang/Object;)V 	drawImage 3(Ljava/awt/Image;IILjava/awt/image/ImageObserver;)Z dispose java/awt/RenderingHints$Key ! ` a  b c   h i    j k    l k    m k    n k    o k    p k    q k    r k    s t    u v    w k    x k    y k    z k    { k    | k    } ~     ~    � k    � k    � k    � k    � k     � �  �   �     �*� 
*� *� *� *� *� *� *� *� *� Y*� � *� Y� � *� � � *� Y� � �  � **� � � !�  � L+� #� $%� &*� '�  F u x "  �    � e  �  B �  � �  �        *� �      � �  �        *� �      � �  �        *� �      � �  �        
*� (� ) �      � �  �        
*� *� ) �      � �  �        *� �      � �  �  �  	  �*Y� '#b� '*� '*� �� N*� **� *� *� *� *� ) j� +�� , *� (*� *� *� *� (� ) j� +�� , *� '*� (#� - W*� *#� - W*� (� ) *� *� ) *� njE**� *� *� ) *� � +�� 	**� $*� � +�� *� (� ) �� .�F*� *� ) #j8*� n%j8� /� 0�� q*� %n8*� *� �� 2�jf8*� *� �� 3�jb8**� b�� 2�jb� **� b�� 3�jf� **� b� 4s�� � 1**� ��*� �� 3kc�� **� ��*� �� 2kc�� �    �    � a� �  �  -  � �  �       �*+67� 8� 9� *+:7� 8� 9� *+;7� 8� 9� *+<7� 8� 9� *+=7� 8� 9� *+>7� 8� 9� *+?@� 8� 9� A*+B@� 8� 9� C*+D7� 8� 9� E*+FG� 8� 9� *+HI� 8� 9� +J7� 8� 9E$�� *� KY$� L� *� *� MY� N� *+O7� 8� 9E$�� *� KY$� L� (� *� MY� N� (�    �   	 � �
 
  � �  �   ]     Q+� P� QM,� R� S,*� � Tc*� �*� �� V,� W� X� Y,*�  *� � Zg�*� \f�� ]W,� ^�      � �  �   U     I**� A� **� C� **� E� **� � '*� *� , *� *� _ *� (� , *� (� _ �     � �  �        *� 	�     � �  �        *� �     � �  �        *#Z� �     � �  �        *� �     � �  �        *#Z� �     � �  �        *� �     � �  �        *� �     � �  �        *� �     � �  �        *� �      f     d `    ` g 3 �4	                                                                                                                                                                                                                                                                                                                             src/com/lib/udacity/simulator/SensorArray.class                                                     0000600 0000000 0000000 00000005606 11757604526 020663  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 �
 4 W	 3 X	 3 Y	 3 Z	 3 [	 3 \	 3 ] ^
  W	 3 _	 3 ` 8 a
 b c
 d e : = f
 " g h i j
 k l
 k m n o n p
 q r
  s t u
  v
 q w
 q x y
 " z
  {
  | }
  ~ 
 " �
  �	 3 �
 k �
 3 � � �
 3 � � �
 3 � � � � � � r Lcom/lib/util/Random; gpsSensorNoise F cameraImageNoise 	gpsUpdate I cameraUpdate scannerUpdate scannerRange c 
simulation &Lcom/lib/udacity/simulator/Simulation; <init> )(Lcom/lib/udacity/simulator/Simulation;)V Code loadProperties (Ljava/util/Properties;)V getCameraImage ()[[I StackMapTable � � getScannerDots u getGPSPosition ()[F onPaint (Ljava/awt/Graphics2D;)V init ()V update (F)V C T 8 9 : 9 ; < = < > < ? < com/lib/util/Random 6 7 A B 0 � � � � � � 10 � � gpsSensorUpdate laserScannerUpdate laserScannerRange � � � � � � � � � � � � � � � [I java/util/ArrayList C � � � � � java/lang/Integer � � � � � � [[I � � [Ljava/lang/Integer; � � � � @ < � � O P � � � H I � � M I � � %com/lib/udacity/simulator/SensorArray java/lang/Object 4com/lib/udacity/simulator/abstracts/SimulationObject 'com/lib/udacity/simulator/abstracts/Car com/lib/udacity/simulator/World java/util/Properties getProperty 8(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String; java/lang/Float 
parseFloat (Ljava/lang/String;)F parseInt (Ljava/lang/String;)I $com/lib/udacity/simulator/Simulation getCar +()Lcom/lib/udacity/simulator/abstracts/Car; getWorld #()Lcom/lib/udacity/simulator/World; getX ()F getY getColorAtPixel (FF)I 	nextFloat (I)V 
getSpacint ()I isInsideWall (II)Z valueOf (I)Ljava/lang/Integer; add (Ljava/lang/Object;)Z size get (I)Ljava/lang/Object; intValue nextGaussian (FF)D getListener :()Lcom/lib/udacity/simulator/abstracts/SimulationListener; 6com/lib/udacity/simulator/abstracts/SimulationListener onGPS ([F)V onCamera ([[I)V 	onScanner ! 3 4  5 	  6 7    8 9    : 9    ; <    = <    > <    ? <    @ <    A B     C D  E   ?     3*� *� *� *� *� *� *� *� Y� 	� 
*+� �      F G  E   g     [*+� � � *+� � � *+� � � *+� � � *+� � � *+� � � �      H I  E   e     G*� � L*� � M,+�  +�  � >*� 
� *� f�� 	`~>� Y�
YOS�    J    � 8 K L  M I  E       ܻ Y*� *� h� L*� � �  =*� t>*� � o*� � �  �6*� t6*� � I*� � �  �6*� � ``� !� +� "Y� #SY� #S� $W`6���`>���+� %� &N6+� %� 1-2+� '� (2� )O-2+� '� (2� )O����-�    J   " � " N� � E� � �  &� 6  O P  E   F     :*� � L*� 
+�  *� � *�E*� 
+�  *� � *�F�Y$QY%Q�      Q R  E         �      S T  E        *� +�      U V  E   v     _*Y� +`� +*� +*� p� *� � ,*� -� . *� +*� p� *� � ,*� /� 0 *� +*� p� *� � ,*� 1� 2 �    J    &                                                                                                                            src/com/lib/udacity/simulator/Simulation.class                                                      0000600 0000000 0000000 00000007724 11757604526 020542  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 �
 3 s	 2 t	 2 u v
  s	 2 w x
  y z
 	 s {
  s | }	 2 ~	 2 	 2 �	 2 �	 2 �	 2 �	 2 � �
  �
  � �
  s �
  �
  � | � � � � � � � �   � � � � �
 2 �
 2 �
 � �<��
 � �   �
 � �
 � �
  � �
 . � | �	 2 � � � � � car )Lcom/lib/udacity/simulator/abstracts/Car; world !Lcom/lib/udacity/simulator/World; run Z listener 8Lcom/lib/udacity/simulator/abstracts/SimulationListener; 	timeDelay I currentThread Ljava/lang/Thread; goalX goalY visual 0Lcom/lib/udacity/simulator/view/SimulationPanel; objects Ljava/util/List; 	Signature HLjava/util/List<Lcom/lib/udacity/simulator/abstracts/SimulationObject;>; runa <init> ()V Code getGoalX ()I getGoalY setGoalX (I)V setGoalY getCar +()Lcom/lib/udacity/simulator/abstracts/Car; getWorld #()Lcom/lib/udacity/simulator/World; getListener :()Lcom/lib/udacity/simulator/abstracts/SimulationListener; getTimeDelay setListener ;(Lcom/lib/udacity/simulator/abstracts/SimulationListener;)V 
setRunning (Z)V 	isRunning ()Z setPanel 3(Lcom/lib/udacity/simulator/view/SimulationPanel;)V setTimeDelay start StackMapTable 
loadConfig (Ljava/lang/String;)V � � 
Exceptions � � � iterator ()Ljava/util/Iterator; N()Ljava/util/Iterator<Lcom/lib/udacity/simulator/abstracts/SimulationObject;>; <clinit> rLjava/lang/Object;Ljava/lang/Runnable;Ljava/lang/Iterable<Lcom/lib/udacity/simulator/abstracts/SimulationObject;>; K L : ; > ? java/util/LinkedList F G %com/lib/udacity/simulator/SensorArray K � $com/lib/udacity/simulator/DefaultCar com/lib/udacity/simulator/World � � � 6 7 8 9 B ? C ? < = D E @ A java/lang/Thread K � d L java/util/Properties java/io/FileReader K g � � n o � � ` � � 4com/lib/udacity/simulator/abstracts/SimulationObject � � � � L � � � � � � ] ^ _ ` � � � � � � � � � L � L � � java/lang/InterruptedException � L J ; $com/lib/udacity/simulator/Simulation java/lang/Object java/lang/Runnable java/lang/Iterable java/util/Iterator java/io/FileNotFoundException java/io/IOException )(Lcom/lib/udacity/simulator/Simulation;)V java/util/List add (Ljava/lang/Object;)Z (Ljava/lang/Runnable;)V load (Ljava/io/Reader;)V hasNext next ()Ljava/lang/Object; 0com/lib/udacity/simulator/abstracts/Configurable loadProperties (Ljava/util/Properties;)V init 'com/lib/udacity/simulator/abstracts/Car getController 5()Lcom/lib/udacity/simulator/abstracts/CarController; 6com/lib/udacity/simulator/abstracts/SimulationListener f(Lcom/lib/udacity/simulator/abstracts/CarController;Lcom/lib/udacity/simulator/abstracts/Background;)V java/lang/System currentTimeMillis ()J onUpdate (F)V update .com/lib/udacity/simulator/view/SimulationPanel repaint 
revalidate sleep (J)V printStackTrace ! 2 3  4 5   6 7    8 9    : ;    < =    > ?    @ A    B ?    C ?    D E    F G  H    I 	 J ;     K L  M   k     _*� *� *� *� Y� � � Y*� L� 	Y� 
M� Y� N*� -�  W*� ,�  W*� +�  W*,� *-� �      N O  M        *� �      P O  M        *� �      Q R  M        *� �      S R  M        *� �      T U  M        *� �      V W  M        *� �      X Y  M        *� �      Z O  M        *� �      [ \  M        *+� �     ! ] ^  M        *� �     ! _ `  M        *� �      a b  M        *+� �      c R  M        *� �      d `  M   3     *� � *� Y*� � *� � ��    e      f g  M   ^     >� Y� M,� Y+� � *� �  N-�  � -�  �  :,� ! ���    e    �  h i�  j     k l  : L  M   �     �*� � �*� �  L+�  � +�  �  M,� " ���*� *� � # *� � $ *� %*� &� ���� '@*� (� ) *� �  N-�  � -�  �  :(� * ���*� � *� � +*� � ,� 'e@*� �e@	�� � -� N-� /���  � � � .  e   ! � 	 i� 	�  i� B m�   n o  M        
*� � 0 �     H    p  q L  M         � 1�      H    r                                            src/com/lib/udacity/simulator/view/                                                                 0000700 0000000 0000000 00000000000 11762166564 016326  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/lib/udacity/simulator/view/ControlPanel.class                                               0000600 0000000 0000000 00000003371 11753174356 021761  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 w
  5	  6 7 8
  9	  :
  ; <
  =	  >
  ?
  @ A
  5
  B C
  D E
 F G
 H I
 H J K
  L
 H M	 H N
 O P
 O Q
  R
 H S T U V W serialVersionUID J ConstantValue        
simulation &Lcom/lib/udacity/simulator/Simulation; btnStart Ljavax/swing/JButton; speed Ljavax/swing/JSlider; <init> )(Lcom/lib/udacity/simulator/Simulation;)V Code actionPerformed (Ljava/awt/event/ActionEvent;)V StackMapTable stateChanged "(Ljavax/swing/event/ChangeEvent;)V - X ' ( javax/swing/JButton Pause - Y ) * Z [ javax/swing/JSlider - \ + , ] ^ _ ` java/awt/BorderLayout a b East c d Center e f g h i j k l Start m Y n j o p q r X s X t u v ` +com/lib/udacity/simulator/view/ControlPanel javax/swing/JPanel java/awt/event/ActionListener  javax/swing/event/ChangeListener ()V (Ljava/lang/String;)V addActionListener "(Ljava/awt/event/ActionListener;)V (II)V addChangeListener %(Ljavax/swing/event/ChangeListener;)V setValue (I)V 	setLayout (Ljava/awt/LayoutManager;)V add )(Ljava/awt/Component;Ljava/lang/Object;)V java/awt/event/ActionEvent 	getSource ()Ljava/lang/Object; $com/lib/udacity/simulator/Simulation 	isRunning ()Z 
setRunning (Z)V setText start visual 0Lcom/lib/udacity/simulator/view/SimulationPanel; .com/lib/udacity/simulator/view/SimulationPanel 
revalidate repaint getValue ()I setTimeDelay !      !   " #  $    %  ' (    ) *    + ,     - .  /   i     ]*� *+� *� Y� � *� *� *� Yd� 	� 
*� 
*� *� 
F� *� Y� � **� � **� 
� �      0 1  /   p     Y+� *� � P*� � � *� � *� � � *� � *� � � *� � *� � � *� � � �    2    )  3 4  /        *� e*� 
� d� �                                                                                                                                                                                                                                                                             src/com/lib/udacity/simulator/view/ControlPanel1.class                                              0000600 0000000 0000000 00000003372 11757604526 022044  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 w
  5	  6 7 8
  9	  :
  ; <
  =	  >
  ?
  @ A
  5
  B C
  D E
 F G
 H I
 H J K
  L
 H M	 H N
 O P
 O Q
  R
 H S T U V W serialVersionUID J ConstantValue        
simulation &Lcom/lib/udacity/simulator/Simulation; btnStart Ljavax/swing/JButton; speed Ljavax/swing/JSlider; <init> )(Lcom/lib/udacity/simulator/Simulation;)V Code actionPerformed (Ljava/awt/event/ActionEvent;)V StackMapTable stateChanged "(Ljavax/swing/event/ChangeEvent;)V - X ' ( javax/swing/JButton Pause - Y ) * Z [ javax/swing/JSlider - \ + , ] ^ _ ` java/awt/BorderLayout a b East c d Center e f g h i j k l Start m Y n j o p q r X s X t u v ` ,com/lib/udacity/simulator/view/ControlPanel1 javax/swing/JPanel java/awt/event/ActionListener  javax/swing/event/ChangeListener ()V (Ljava/lang/String;)V addActionListener "(Ljava/awt/event/ActionListener;)V (II)V addChangeListener %(Ljavax/swing/event/ChangeListener;)V setValue (I)V 	setLayout (Ljava/awt/LayoutManager;)V add )(Ljava/awt/Component;Ljava/lang/Object;)V java/awt/event/ActionEvent 	getSource ()Ljava/lang/Object; $com/lib/udacity/simulator/Simulation 	isRunning ()Z 
setRunning (Z)V setText start visual 0Lcom/lib/udacity/simulator/view/SimulationPanel; .com/lib/udacity/simulator/view/SimulationPanel 
revalidate repaint getValue ()I setTimeDelay !      !   " #  $    %  ' (    ) *    + ,     - .  /   i     ]*� *+� *� Y� � *� *� *� Yd� 	� 
*� 
*� *� 
F� *� Y� � **� � **� 
� �      0 1  /   p     Y+� *� � P*� � � *� � *� � � *� � *� � � *� � *� � � *� � � �    2    )  3 4  /        *� e*� 
� d� �                                                                                                                                                                                                                                                                            src/com/lib/udacity/simulator/view/ControlPanel2.class                                              0000600 0000000 0000000 00000003333 11757604526 022042  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 ~
 $ 8	 # 9 : ;
  <	 # =
  > ?
  @	 # A B
  C	 # D E F
  8
 # G H
 # I J K
 L M
  N
 O P	 Q R S
  8
  T U
  V
  W
 X Y
 Z [
 Z \ ] ^ _ serialVersionUID J ConstantValue        
simulation &Lcom/lib/udacity/simulator/Simulation; btnGoal Ljavax/swing/JButton; goalX Ljavax/swing/JTextField; goalY <init> )(Lcom/lib/udacity/simulator/Simulation;)V Code actionPerformed (Ljava/awt/event/ActionEvent;)V StackMapTable 2 ` + , javax/swing/JButton Change Goal 2 a - . b c javax/swing/JTextField 2 d / 0 770 e a 1 0 570 java/awt/BorderLayout f g East h i West Center j k l m n o p q r s t java/lang/StringBuilder u v  -  u w x n y z a { | d } d ,com/lib/udacity/simulator/view/ControlPanel2 javax/swing/JPanel java/awt/event/ActionListener ()V (Ljava/lang/String;)V addActionListener "(Ljava/awt/event/ActionListener;)V (I)V setText 	setLayout (Ljava/awt/LayoutManager;)V add )(Ljava/awt/Component;Ljava/lang/Object;)V java/awt/event/ActionEvent 	getSource ()Ljava/lang/Object; getText ()Ljava/lang/String; java/lang/Integer parseInt (Ljava/lang/String;)I java/lang/System out Ljava/io/PrintStream; append (I)Ljava/lang/StringBuilder; -(Ljava/lang/String;)Ljava/lang/StringBuilder; toString java/io/PrintStream print $com/lib/udacity/simulator/Simulation setGoalX setGoalY ! # $  %   & '  (    )  + ,    - .    / 0    1 0     2 3  4   �     t*� *+� *� Y� � *� *� *� Y#� 	� 
*� 
� *� Y#� 	� *� � *� Y� � **� � **� 
� **� � �      5 6  4   f     O+� *� � F*� 
� � =*� � � >� � Y� � � � � �  *� � !*� � "�    7    � N                                                                                                                                                                                                                                                                                                       src/com/lib/udacity/simulator/view/SimulationFrame.class                                            0000600 0000000 0000000 00000002462 11757604526 022461  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 R
  ( )
  *	  +
 , - .
  *	  / 0
 	 *	  1 2
  (
  3 4
  5 6 7
 , 8
 9 :
 9 ;
  <
  = > ? serialVersionUID J ConstantValue        simulationPanel 0Lcom/lib/udacity/simulator/view/SimulationPanel; controlPanel1 .Lcom/lib/udacity/simulator/view/ControlPanel1; controlPanel2 .Lcom/lib/udacity/simulator/view/ControlPanel2; <init> )(Lcom/lib/udacity/simulator/Simulation;)V Code % @ .com/lib/udacity/simulator/view/SimulationPanel % &    A B C ,com/lib/udacity/simulator/view/ControlPanel1 ! " ,com/lib/udacity/simulator/view/ControlPanel2 # $ java/awt/BorderLayout D E Center F G North South H I J K L M L N O P Q .com/lib/udacity/simulator/view/SimulationFrame javax/swing/JFrame ()V $com/lib/udacity/simulator/Simulation setPanel 3(Lcom/lib/udacity/simulator/view/SimulationPanel;)V 	setLayout (Ljava/awt/LayoutManager;)V add )(Ljava/awt/Component;Ljava/lang/Object;)V getWorld #()Lcom/lib/udacity/simulator/World; com/lib/udacity/simulator/World getWidth ()I 	getHeight 	setBounds (IIII)V setDefaultCloseOperation (I)V !                      ! "    # $     % &  '   �     {*� *� Y+� � +*� � *� Y+� � *� 	Y+� 
� *� Y� � **� � **� � **� � *dd+� � `+� � P`� *� �                                                                                                                                                                                                                    src/com/lib/udacity/simulator/view/SimulationPanel.class                                            0000600 0000000 0000000 00000005211 11757604526 022461  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 �
  =	  >
  ?
  @ A
 B C D E D F G 	 H
 B I J H	 B K
 L M
 L N
 L O
 P Q	  R
 P S	  T	  U	  V	 L W	 X Y Z
  [ \ ]
  ^
  _ ` a b serialVersionUID J ConstantValue        
simulation &Lcom/lib/udacity/simulator/Simulation; px I py pbx pby <init> )(Lcom/lib/udacity/simulator/Simulation;)V Code paint (Ljava/awt/Graphics;)V StackMapTable A c mousePressed (Ljava/awt/event/MouseEvent;)V mouseReleased ` d mouseEntered mouseClicked mouseExited - e & ' f g 0 1 java/awt/Graphics2D h i j c k l m n 4com/lib/udacity/simulator/abstracts/SimulationObject o p q r s t u v w x y x z x d { x ( ) | x * ) + ) , ) } ~  � � java/awt/Rectangle - � � � � � e � e .com/lib/udacity/simulator/view/SimulationPanel javax/swing/JPanel java/awt/event/MouseListener java/util/Iterator java/awt/event/MouseEvent ()V addMouseListener !(Ljava/awt/event/MouseListener;)V $com/lib/udacity/simulator/Simulation iterator ()Ljava/util/Iterator; hasNext ()Z next ()Ljava/lang/Object; onPaint (Ljava/awt/Graphics2D;)V getListener :()Lcom/lib/udacity/simulator/abstracts/SimulationListener; 6com/lib/udacity/simulator/abstracts/SimulationListener world !Lcom/lib/udacity/simulator/World; com/lib/udacity/simulator/World 
getSpacint ()I 	getHeight getWidth getX getY wallMap #Lcom/lib/udacity/simulator/WallMap; !com/lib/udacity/simulator/WallMap rects Ljava/util/List; (IIII)V java/util/List add (Ljava/lang/Object;)Z 
revalidate repaint !        ! "  #    $  & '    ( )    * )    + )    , )     - .  /        *� *+� **� �      0 1  /   _     ?*+� +� M*� � N-�  � -�  � 	:,� 
 ���*� � ,�  �    2    �  3 4�   5 6  /   �     �*� � � =*� � � >*� � � 6*+� � *� � *� � *� � 	*� *+� � *� � *� � *� � *� **� l� **� l� �    2    � 9  7 6  /  �  	  �*� � � =*� � � >*� � � 6+� 6� 	6� � 	d6+� 6� 	6� � 	d6l6l6*� � �*� � B*� � � � � Y*� h*� h*� dh*� dh� �  W� �*� � � � � Y*� hh*� dh*� dh� �  W� �*� � @*� � � � � Yh*� h*� dh*� dh� �  W� =*� � � � � Y*� hh*� dh*� dh� �  W*� *� �    2   # � 3  8 9  � � ^<� E9  : 6  /         �      ; 6  /   �  	   �*� � � =*� � � >*� � � 6+� 6� 	6� � 	d6+� 6� 	6� � 	d6l6l6*� � � � � Yhh

� �  W*� *� �    2    � 3  8 9  �   < 6  /         �                                                                                                                                                                                                                                                                                                                                                                                             src/com/lib/udacity/simulator/WallMap.class                                                         0000600 0000000 0000000 00000003100 11757604526 017733  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 p
  / 0
  /	  1 2 3
  4
  5
  6 7
 8 9
 8 : ;
 < =
  > ? @
  A ? B C D C E
  F	 G H
 I J
 I K L M rects Ljava/util/List; 	Signature &Ljava/util/List<Ljava/awt/Rectangle;>; <init> ()V Code loadFromFile (Ljava/io/File;)V StackMapTable 2 N O 
Exceptions P isInsideWall (II)Z Q paint (Ljava/awt/Graphics2D;)V    java/util/LinkedList   java/io/BufferedReader java/io/FileReader  #  R S T , N U V W X java/awt/Rectangle Y Z [  \ ] ^ _ `   a b Q c d e f g + h i j k l m n o !com/lib/udacity/simulator/WallMap java/lang/Object java/lang/String [Ljava/lang/String; java/lang/Exception java/util/Iterator (Ljava/io/Reader;)V readLine ()Ljava/lang/String; split '(Ljava/lang/String;)[Ljava/lang/String; charAt (I)C java/lang/Integer parseInt (Ljava/lang/String;)I (IIII)V java/util/List add (Ljava/lang/Object;)Z close iterator ()Ljava/util/Iterator; hasNext ()Z next ()Ljava/lang/Object; contains java/awt/Color 	DARK_GRAY Ljava/awt/Color; java/awt/Graphics2D setColor (Ljava/awt/Color;)V fill (Ljava/awt/Shape;)V !                     !        *� *� Y� � �      " #  !   �     q� Y� Y+� � MN,� 	YN� T-
� :2� �   >      r   *� � Y2� 2� 2� 2� � �  W���,� �    $    �  % &� ) '� , (     )  * +  !   M     /*� �  N-�  � -�  � :� � �����    $    � 
 ,�   - .  !   J     -+� � *� �  M,�  � ,�  � N+-� ���    $    �  ,�                                                                                                                                                                                                                                                                                                                                                                                                                                                                   src/com/lib/udacity/simulator/World.class                                                           0000600 0000000 0000000 00000006266 11757604526 017505  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 �
 7 ` a
  `	 6 b c
  `	 6 d	 6 e	 6 f	 6 g
  h i j
 k l
 m n o p q r s t
  u A	 6 v w x y z
 { |
  u
  } ~	  � �
 � �
   � �
 % �	 6 �
 % �	 � �
 � �
 � �
 6 �	 � �	 � �
 � �
 � �
  �
 � �
  �
 6 �
 6 � � � � � � r Lcom/lib/util/Random; width I height 
background [[I 	bgSpacing bgImage Ljava/awt/image/BufferedImage; wallMap #Lcom/lib/udacity/simulator/WallMap; <init> ()V Code 
getSpacint ()I 	getHeight getWidth isInsideWall (II)Z loadProperties (Ljava/util/Properties;)V StackMapTable ~ bufferBackground � randomBackground onPaint (Ljava/awt/Graphics2D;)V init update (F)V 
getColorAt (II)I getColorAtPixel (FF)I G H com/lib/util/Random ; < !com/lib/udacity/simulator/WallMap E F B > ? > = > N O worldSpacing 5 � � � � � � 
worldWidth 800 worldHeight 600 "java/lang/IllegalArgumentException ,Height/Width should be devidable by spacing! G � @ A mapFile java/io/File "   � � � � � java/lang/Exception � � � Error loading Map File! � � � � H java/awt/image/BufferedImage G � C D � � � � � � � � � � ^ _ � � � � � � � H � � � � � � X V H T H com/lib/udacity/simulator/World java/lang/Object 0com/lib/udacity/simulator/abstracts/Configurable 4com/lib/udacity/simulator/abstracts/SimulationObject .com/lib/udacity/simulator/abstracts/Background java/awt/Graphics java/util/Properties getProperty 8(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String; java/lang/Integer parseInt (Ljava/lang/String;)I (Ljava/lang/String;)V java/lang/String replace D(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String; loadFromFile (Ljava/io/File;)V java/lang/System err Ljava/io/PrintStream; java/io/PrintStream println printStackTrace (III)V createGraphics ()Ljava/awt/Graphics2D; java/awt/Color black Ljava/awt/Color; setColor (Ljava/awt/Color;)V drawLine (IIII)V white gray fillRect dispose nextInt (I)I java/awt/Graphics2D 	drawImage 3(Ljava/awt/Image;IILjava/awt/image/ImageObserver;)Z paint ! 6 7  8 9 :   ; <    = >    ? >    @ A    B >    C D    E F     G H  I   '     *� *� Y� � *� Y� � �      J K  I        *� �      L K  I        *� 	�      M K  I        *� 
�      N O  I        
*� � �      P Q  I   �     �*+� � � *+� � � 
*+� � � 	*� 
*� p� *� 	*� p� � Y� �**� 
*� 	� � +� M,� *� � Y,� � � � M� !"� #,� $�  _ � �    R    � E	1B S  T H  I   �     �*� %Y*� 
*� 	� &� '*� '� (L=*� 
� s+� )� *+*� 	� +>*� 	� M+� )� *+*� 
� +*��� ,� +� -� *� 
+� .� *+`*� d*� � /*� `>���*� `=���+� )� *+*� 
d*� 
d*� 	d� ++*� 	d*� 
d*� 	d� ++� 0�    R    �  U� .� � 	  V H  I   S     1<*� 
� )=*� 	� *� 2*� � 1O������ձ    R    � � 	� �   W X  I   !     +*� '� 2W*� +� 3�      Y H  I        	*� 4*� 5�      Z [  I         �      \ ]  I   =     '*� �� � � *� 2�� �*� 2.�    R      ^ _  I   W     =#*� �n�>$*� �n�6*� �� � � *� 2�� �*� 2.�    R    � 1                                                                                                                                                                                                                                                                                                                                            src/com/lib/util/                                                                                   0000700 0000000 0000000 00000000000 11762166564 012650  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/lib/util/Random.class                                                                       0000600 0000000 0000000 00000000535 11757604526 015123  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   ����   2 
  
     serialVersionUID J ConstantValue�#%��)�< <init> ()V Code nextGaussian (F)D (FF)D StackMapTable 
    com/lib/util/Random java/util/Random ()D !                 
           *� �     !            *� #�c�     !       )     $�� #��*� $�k#�c�        	                                                                                                                                                                     src/com/udacity/                                                                                    0000700 0000000 0000000 00000000000 11762166563 012566  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/udacity/simulator/                                                                          0000700 0000000 0000000 00000000000 11762166563 014605  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/udacity/simulator/abstracts/                                                                0000700 0000000 0000000 00000000000 11762166564 016574  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/udacity/simulator/abstracts/Background.java                                                 0000600 0000000 0000000 00000000233 11743745404 021511  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.abstracts;

public interface Background 
{
	int getColorAtPixel(float x, float y);
	int getColorAt(int x, int y);
}                                                                                                                                                                                                                                                                                                                                                                     src/com/udacity/simulator/abstracts/Background.java~                                                0000600 0000000 0000000 00000000252 11725163624 021706  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.udacity.simulator.abstracts;

public interface Background 
{
	int getColorAtPixel(float x, float y);
	int getColorAt(int x, int y);
}
                                                                                                                                                                                                                                                                                                                                                      src/com/udacity/simulator/abstracts/Car.java                                                        0000600 0000000 0000000 00000000414 11743745362 020143  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.abstracts;

public interface Car extends SimulationObject
{
	public float getX();
	public float getY();
	public float getAngle();
	public float getSteer();
	public float getSpeed();
	public CarController getController();
}
                                                                                                                                                                                                                                                    src/com/udacity/simulator/abstracts/Car.java~                                                       0000600 0000000 0000000 00000000431 11725111150 020316  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.udacity.simulator.abstracts;

public interface Car extends SimulationObject
{
	public float getX();
	public float getY();
	public float getAngle();
	public float getSteer();
	public float getSpeed();
	public CarController getController();
}
                                                                                                                                                                                                                                       src/com/udacity/simulator/abstracts/CarController.java                                              0000600 0000000 0000000 00000000522 11743745352 022206  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.abstracts;

public interface CarController 
{
	public float getSpeed();
	public float getGyro();
	
	/**
	 * @param s - Speed from 1 (max) to -1 (max reverse)
	 */
	public void setSpeed(float s);
	/**
	 * @param s - Steer from 1 (left) to -1 (right)
	 */
	public void setSteer(float s);
}
                                                                                                                                                                              src/com/udacity/simulator/abstracts/CarController.java~                                             0000600 0000000 0000000 00000000537 11741266052 022403  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.udacity.simulator.abstracts;

public interface CarController 
{
	public float getSpeed();
	public float getGyro();
	
	/**
	 * @param s - Speed from 1 (max) to -1 (max reverse)
	 */
	public void setSpeed(float s);
	/**
	 * @param s - Steer from 1 (left) to -1 (right)
	 */
	public void setSteer(float s);
}
                                                                                                                                                                 src/com/udacity/simulator/abstracts/Configurable.java                                               0000600 0000000 0000000 00000000312 11743745336 022034  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.abstracts;

import java.util.Properties;

//TODO: find reason for this interface
public interface Configurable 
{
	public void loadProperties(Properties p);
}
                                                                                                                                                                                                                                                                                                                      src/com/udacity/simulator/abstracts/Configurable.java~                                              0000600 0000000 0000000 00000000327 11724457024 022231  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.udacity.simulator.abstracts;

import java.util.Properties;

//TODO: find reason for this interface
public interface Configurable 
{
	public void loadProperties(Properties p);
}
                                                                                                                                                                                                                                                                                                         src/com/udacity/simulator/abstracts/SimulationListener.java                                         0000600 0000000 0000000 00000000556 11743745326 023277  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.abstracts;

import java.awt.Graphics2D;

public interface SimulationListener
{
	public void init(CarController crtl, Background background);
	public void onUpdate(float dt);
	public void onGPS(float[] pos);
	public void onCamera(int[][] img);
	public void onPaint(Graphics2D g);
	public void onScanner(int[][] dots);
}
                                                                                                                                                  src/com/udacity/simulator/abstracts/SimulationListener.java~                                        0000600 0000000 0000000 00000000556 11743745326 023475  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.abstracts;

import java.awt.Graphics2D;

public interface SimulationListener
{
	public void init(CarController crtl, Background background);
	public void onUpdate(float dt);
	public void onGPS(float[] pos);
	public void onCamera(int[][] img);
	public void onPaint(Graphics2D g);
	public void onScanner(int[][] dots);
}
                                                                                                                                                  src/com/udacity/simulator/abstracts/SimulationObject.java                                           0000600 0000000 0000000 00000000350 11743745316 022707  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.abstracts;

import java.awt.Graphics2D;

public interface SimulationObject extends Configurable
{
	public void init();
	public void update(float dt);
	public void onPaint(Graphics2D g);
}
                                                                                                                                                                                                                                                                                        src/com/udacity/simulator/abstracts/SimulationObject.java~                                          0000600 0000000 0000000 00000000365 11725113154 023100  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.jreitter.philipp.udacity.simulator.abstracts;

import java.awt.Graphics2D;

public interface SimulationObject extends Configurable
{
	public void init();
	public void update(float dt);
	public void onPaint(Graphics2D g);
}
                                                                                                                                                                                                                                                                           src/com/udacity/simulator/BicycleModel.java                                                         0000600 0000000 0000000 00000001722 11743745414 020004  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator;

public class BicycleModel 
{
	//when i did the exact same calculation in python it would just drift apart from the java calculation
	public static float[] getPos(float x, float y, float angle, float steer, float speed, float dt, float length)
	{
     	float tan = (float)Math.tan(steer);
		float dist = speed*dt;
      float b = (dist/length) * tan;
        
        if(Math.abs(b) >= 0.001)
        {
            float R = length/tan;
            float cx = (x - (float)Math.sin(angle) * R);
            float cy = (y + (float)Math.cos(angle) * R);
            x = (cx + (float)Math.sin(angle+b) * R);
            y = (cy - (float)Math.cos(angle+b) * R);
            angle = (float)((angle+b)%(2.*Math.PI));
        }
        else
        {
            x = (float)(x + dist * Math.cos(angle));
            y = (float)(y + dist * Math.sin(angle));
        }
        
        return new float[]{x, y, angle};
	}
}
                                              src/com/udacity/simulator/DefaultCar.java                                                           0000600 0000000 0000000 00000013625 11743745236 017472  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.RenderingHints;
import java.io.File;
import java.util.Properties;

import javax.imageio.ImageIO;

import com.lib.controller.Element;
import com.lib.controller.Link;
import com.lib.controller.PT1;
import com.lib.udacity.simulator.abstracts.Car;
import com.lib.udacity.simulator.abstracts.CarController;
import com.lib.udacity.simulator.abstracts.Configurable;
import com.lib.util.Random;

public class DefaultCar implements Car, Configurable
{
	private Image carImage;
	
	/**
	 * CarController class is used for data encapsulation.
	 * While user gets noisy values from the controller, 
	 * the simulation can get real values from Car class.
	 * As long as we don't give the Car to user we are fine.
	 * 
	 * thats deprecated, since i want real the focus is no more on 
	 * pure localization, i want real values for path planning
	 */
	public class DefaultCarController implements CarController
	{
		private DefaultCarController()
		{
		}
		
		public float getSpeed(){return retSpeed;}
		public float getGyro(){return retGyro;}
		
		public void setSpeed(float s)
		{
			if(s>1.f)s=1.f;
			else if(s<-1.f)s=-1.f;
		
			desiredSpeed = s*maxSpeed;
		}

		public void setSteer(float s)
		{
			if(s>1.f)s=1.f;
			else if(s<-1.f)s=-1.f;
		
			desiredSteer = s*maxSteer;
		}
		
		public float[] getPos()
		{
			return new float[]{x,y};
		}
		
		public float getAngle()
		{
			return angle;
		}
	}
	
	//Configuration Variables
	private float speedSensorError = 0.f;
	private float gyroSensorError = 0.f;
	
	private float steerError = 0.f;
	private float speedError = 0.f;
	
	private float maxSpeed = 0.f;
	private float maxSteer = 0.f;

	private float randomTime = 0.5f;
	
	private float carLength = 100.f;
	
	//Other suff
	private Random r;
	private CarController controller;

	//Car State variables
	private float x;
	private float y;
	private float startX;
	private float startY;
	private float startA;
	private float angle;
	
	private Element speed;
	private Element steer;
	
	private float desiredSteer;
	private float desiredSpeed;
	
	//Randomized Values 
	private float retSpeed;
	private float retGyro;
	
	private float time;
	
	//Constructor
	public DefaultCar( )
	{
		controller = new DefaultCarController();
		r = new Random( );
		
		try
		{
			if( getClass().getResource("/img/car.png") == null )
				carImage = ImageIO.read(new File("img/car.png")); //really fast hotfix
			else
				carImage = ImageIO.read(getClass().getResource("/img/car.png"));
		}catch(Exception e)
		{
			e.printStackTrace();
			System.err.println("Couldn't load img/car.png");
		}
		time = 0;
	}
	
	//Getter&Setter
	public float getX(){return x;}
	public float getY(){return y;}
	public float getAngle(){return angle;}
	public float getSteer(){return steer.value();}
	public float getSpeed(){return speed.value();}
	public CarController getController(){return controller;};
	
	//Update Method
	public void update(float dt)
	{
		time += dt;
		if( time > randomTime )
		{
			speed.input((float)r.nextGaussian(desiredSpeed, speedError*speed.value()));
			steer.input((float)r.nextGaussian(desiredSteer, steerError*steer.value()));
			time = 0;
		}
			
		steer.update(dt);
		speed.update(dt);

		float dAngle = steer.value()*(speed.value()/maxSpeed);
		retSpeed = (float)r.nextGaussian(speed.value(), speedSensorError);
		
		retGyro = (float)r.nextGaussian(dAngle, gyroSensorError);
		
		float tan = (float)Math.tan(steer.value());
		float dist = speed.value()*dt;
        float b = (dist/carLength) * tan;
        
        if(Math.abs(b) >= 0.001)
        {
            float R = carLength/tan;
            float cx = (x - (float)Math.sin(angle) * R);
            float cy = (y + (float)Math.cos(angle) * R);
            x = (cx + (float)Math.sin(angle+b) * R);
            y = (cy - (float)Math.cos(angle+b) * R);
            angle = (float)((angle+b)%(2.*Math.PI));
        }
        else
        {
            x = (float)(x + dist * Math.cos(angle));
            y = (float)(y + dist * Math.sin(angle));
        }
        
	}

	@Override
	public void loadProperties(Properties p) 
	{
		speedSensorError = Float.parseFloat(p.getProperty("carSpeedSensorError", "0"));
		gyroSensorError  = Float.parseFloat(p.getProperty("carGyroSensorError" , "0"));
		steerError 		 = Float.parseFloat(p.getProperty("carSteerError"	   , "0"));
		speedError 		 = Float.parseFloat(p.getProperty("carSpeedError"	   , "0"));
		maxSpeed 		 = Float.parseFloat(p.getProperty("carMaxSpeed"		   , "0"));
		maxSteer 		 = Float.parseFloat(p.getProperty("carMaxSteer"		   , "0"));	
		startX 			 = Float.parseFloat(p.getProperty("carStartX"		   , "200"));
		startY			 = Float.parseFloat(p.getProperty("carStartY"		   , "200"));	
		startA			 = Float.parseFloat(p.getProperty("carStartAngle"	   , "0"));	
		randomTime		 = Float.parseFloat(p.getProperty("errorUpdateTime"	   , "0.5"));	
		carLength		 = Float.parseFloat(p.getProperty("carLength"	   	   , "100"));	
		
		float T = Float.parseFloat(p.getProperty("carSpeedT", "0"));
		if(T > 0.f) speed = new PT1(T);
		else speed = new Link();
		
		T = Float.parseFloat(p.getProperty("carSteerT", "0"));
		if(T > 0.f) steer = new PT1(T);
		else steer = new Link();
	}

	@Override
	public void onPaint(Graphics2D g) 
	{
	    Graphics2D gg = (Graphics2D) g.create();
	    gg.setColor(Color.BLUE);
	    gg.rotate(angle+Math.PI/2, x, y);
	    gg.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
	    gg.drawImage(carImage, (int)(x-22.5), (int)(y-50), null);
	    gg.dispose();
	}

	@Override
	public void init() 
	{
		x = startX;
		y = startY;
		angle = startA;	
		time = randomTime;
		speed.input(0); 
		speed.value(0);
		steer.input(0); 
		steer.value(0);
	}
	
}
                                                                                                           src/com/udacity/simulator/SensorArray.java                                                          0000600 0000000 0000000 00000005604 11743745222 017721  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator;

import java.awt.Graphics2D;
import java.util.ArrayList;
import java.util.Properties;

import com.lib.udacity.simulator.abstracts.Car;
import com.lib.udacity.simulator.abstracts.SimulationObject;
import com.lib.util.Random;

public class SensorArray implements SimulationObject
{
	//Why not 1 global static object?
	private Random r;
	
	//Configuration
	private float gpsSensorNoise = 0.f;
	private float cameraImageNoise = 0.f;
	private int gpsUpdate = 0;
	private int cameraUpdate = 0;
	private int scannerUpdate = 0;
	private int scannerRange = 0;
	
	private int c;
	
	private Simulation simulation;
	
	public SensorArray(Simulation s)
	{
		r = new Random();
		this.simulation = s;
	}

	@Override
	public void loadProperties(Properties p) 
	{
		gpsSensorNoise 	 = Float.parseFloat(p.getProperty("gpsSensorNoise"  , "0"));
		cameraImageNoise = Float.parseFloat(p.getProperty("cameraImageNoise", "0"));	
		gpsUpdate = Integer.parseInt(p.getProperty("cameraUpdate","10"));
		cameraUpdate = Integer.parseInt(p.getProperty("gpsSensorUpdate","10"));
		scannerUpdate = Integer.parseInt(p.getProperty("laserScannerUpdate","10"));
		scannerRange = Integer.parseInt(p.getProperty("laserScannerRange","10"));
	}

	public int[][] getCameraImage() 
	{
		Car c = simulation.getCar();
		World w = simulation.getWorld();
				
		int i = w.getColorAtPixel(c.getX(),c.getY());
		if(r.nextFloat()>(1.f-cameraImageNoise)) //cuz [0,1[
		{
			i=(i+1)&1;
		}

		return new int[][]{{i}};
	}
	
	public int[][] getScannerDots()
	{
		ArrayList<Integer[]> dots = new ArrayList<Integer[]>(scannerRange*scannerRange);
		int spacing = simulation.getWorld().getSpacint();
		for(int x = -scannerRange; x < scannerRange; x+=spacing)
		{
			int cx = (int)simulation.getCar().getX();
			for(int y = -scannerRange; y < scannerRange; y+=spacing)
			{
				int cy = (int)simulation.getCar().getY();
				if(simulation.getWorld().isInsideWall(cx+x, cy+y))
					dots.add(new Integer[]{x, y});
			}	
		}

		int[][] res = new int[dots.size()][2];
		for(int i = 0; i < dots.size(); i++)
		{
			res[i][0] = dots.get(i)[0];
			res[i][1] = dots.get(i)[1];
		}
		
		return res;
	}
	
	public float[] getGPSPosition() 
	{
		Car c = simulation.getCar();
		float gx = (float)r.nextGaussian(c.getX(), gpsSensorNoise);
		float gy = (float)r.nextGaussian(c.getY(), gpsSensorNoise);
		return new float[]{gx,gy};
	}

	@Override
	public void onPaint(Graphics2D g) {
		
	}

	@Override
	public void init() 
	{
		c = 0;
	}

	@Override
	public void update(float dt) 
	{
		c++;
		if(c%gpsUpdate==0) 
		{
			simulation.getListener().onGPS(getGPSPosition());
		}
		
		if(c%cameraUpdate==0) 
		{
			simulation.getListener().onCamera(getCameraImage());
		}
		
		if(c%scannerUpdate==0) 
		{
			simulation.getListener().onScanner(getScannerDots());
		}
	}

}
                                                                                                                            src/com/udacity/simulator/Simulation.java                                                           0000600 0000000 0000000 00000007212 11753216030 017561  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Properties;

import com.lib.udacity.simulator.abstracts.Car;
import com.lib.udacity.simulator.abstracts.Configurable;
import com.lib.udacity.simulator.abstracts.SimulationListener;
import com.lib.udacity.simulator.abstracts.SimulationObject;
import com.lib.udacity.simulator.view.SimulationPanel;

public class Simulation implements Runnable, Iterable<SimulationObject>
{
	private Car car;
	public  World world;
	private boolean run = false;
	private SimulationListener listener;
	private int timeDelay = 20;
	private Thread currentThread;
	
	private int goalX;
	private int goalY;

	public SimulationPanel visual;
	private List<SimulationObject> objects;
	
	public Simulation()
	{
		objects = new LinkedList<SimulationObject>();
		
		SensorArray sensors = new SensorArray(this);
		DefaultCar  car     = new DefaultCar();
		World       world   = new World();

		objects.add(world);
		objects.add(car);
		objects.add(sensors);
		
		this.car   = car;
		this.world = world;
	}
	
	public int getGoalX(){return goalX;}
	public int getGoalY(){return goalY;}
	public void setGoalX(int x){goalX = x;}
	public void setGoalY(int y){goalY = y;}

	public Car getCar(){return car;}
	public World getWorld(){return world;}
	public SimulationListener getListener(){return listener;}
	public int getTimeDelay(){return timeDelay;}
	
	public void setListener(SimulationListener l){listener = l;}
	public synchronized void setRunning(boolean b){run = b;}
	public synchronized boolean isRunning(){return run;} 
	public void setPanel(SimulationPanel p){visual = p;}
	public void setTimeDelay(int i){timeDelay = i;}
	
	public boolean start()
	{
		if(currentThread == null)
		{
			currentThread = new Thread(this);
			currentThread.start();
			return true;
		}
		return false;
	}
	
	public void loadConfig(String path) throws FileNotFoundException, IOException
	{
		Properties p = new Properties();
		p.load(new FileReader(path));
		for( Configurable c : objects )
			c.loadProperties(p);
	}
	
	@Override
	public void run()
	{
		if( listener == null )
			return;

		for(SimulationObject o : objects)
			o.init();
		
		listener.init(car.getController(), world);

		setRunning(true);
		while(true)
		{
			while(!isRunning());
			
			long time = System.currentTimeMillis();
			
			listener.onUpdate(0.02f);
			
			for(SimulationObject o : objects)
				o.update(0.02f);
			
			if(visual!=null)
			{
				visual.repaint();
				visual.revalidate();
			}
			
			try {
				time = System.currentTimeMillis()-time;
				time = timeDelay - time;
				if(time > 0)
					Thread.sleep(time); //bad, fix it
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}

	@Override
	public Iterator<SimulationObject> iterator() {
		return objects.iterator();
	}
	
	public static boolean runa = true;
	/*
	@SuppressWarnings("deprecation")
	public static void main(String[] args) throws InterruptedException, IOException
	{
		
		Thread d = new Thread()
		{ 
			long start = 0;
			public void run()
			{
				while(runa)
				{
					if( start == 0) start = System.currentTimeMillis();
					System.out.println(System.currentTimeMillis()-start);
					try {
						Thread.sleep(10);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		};
		d.run();
		
		while( System.in.read() == -1) Thread.sleep(10);
		
		runa = false;
		d.stop(); 
	}*/
}
                                                                                                                                                                                                                                                                                                                                                                                      src/com/udacity/simulator/Simulation.java~                                                          0000600 0000000 0000000 00000007212 11753213570 017765  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Properties;

import com.lib.udacity.simulator.abstracts.Car;
import com.lib.udacity.simulator.abstracts.Configurable;
import com.lib.udacity.simulator.abstracts.SimulationListener;
import com.lib.udacity.simulator.abstracts.SimulationObject;
import com.lib.udacity.simulator.view.SimulationPanel;

public class Simulation implements Runnable, Iterable<SimulationObject>
{
	private Car car;
	public  World world;
	private boolean run = false;
	private SimulationListener listener;
	private int timeDelay = 20;
	private Thread currentThread;
	
	private int goalX;
	private int goalY;

	public SimulationPanel visual;
	private List<SimulationObject> objects;
	
	public Simulation()
	{
		objects = new LinkedList<SimulationObject>();
		
		SensorArray sensors = new SensorArray(this);
		DefaultCar  car     = new DefaultCar();
		World       world   = new World();

		objects.add(world);
		objects.add(car);
		objects.add(sensors);
		
		this.car   = car;
		this.world = world;
	}
	
	public int getGoalX(){return goalX;}
	public int getGoalY(){return goalY;}
	public void setGoalX(int x){goalX = x;}
	public void setGoalY(int y){goalY = y;}

	public Car getCar(){return car;}
	public World getWorld(){return world;}
	public SimulationListener getListener(){return listener;}
	public int getTimeDelay(){return timeDelay;}
	
	public void setListener(SimulationListener l){listener = l;}
	public synchronized void setRunning(boolean b){run = b;}
	public synchronized boolean isRunning(){return run;} 
	public void setPanel(SimulationPanel p){visual = p;}
	public void setTimeDelay(int i){timeDelay = i;}
	
	public boolean start()
	{
		if(currentThread == null)
		{
			currentThread = new Thread(this);
			currentThread.start();
			return true;
		}
		return false;
	}
	
	public void loadConfig(String path) throws FileNotFoundException, IOException
	{
		Properties p = new Properties();
		p.load(new FileReader(path));
		for( Configurable c : objects )
			c.loadProperties(p);
	}
	
	@Override
	public void run()
	{
		if( listener == null )
			return;

		for(SimulationObject o : objects)
			o.init();
		
		listener.init(car.getController(), world);

		setRunning(true);
		while(true)
		{
			while(!isRunning());
			
			long time = System.currentTimeMillis();
			
			listener.onUpdate(0.02f);
			
			for(SimulationObject o : objects)
				o.update(0.02f);
			
			if(visual!=null)
			{
				visual.repaint();
				visual.revalidate();
			}
			
			try {
				time = System.currentTimeMillis()-time;
				time = timeDelay - time;
				if(time > 0)
					Thread.sleep(time); //bad, fix it
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}

	@Override
	public Iterator<SimulationObject> iterator() {
		return objects.iterator();
	}
	
	public static boolean runa = true;
	/*
	@SuppressWarnings("deprecation")
	public static void main(String[] args) throws InterruptedException, IOException
	{
		
		Thread d = new Thread()
		{ 
			long start = 0;
			public void run()
			{
				while(runa)
				{
					if( start == 0) start = System.currentTimeMillis();
					System.out.println(System.currentTimeMillis()-start);
					try {
						Thread.sleep(10);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		};
		d.run();
		
		while( System.in.read() == -1) Thread.sleep(10);
		
		runa = false;
		d.stop(); 
	}*/
}
                                                                                                                                                                                                                                                                                                                                                                                      src/com/udacity/simulator/view/                                                                     0000700 0000000 0000000 00000000000 11762166563 015557  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/udacity/simulator/view/ControlPanel1.java                                                   0000600 0000000 0000000 00000004361 11753175534 021107  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.view;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Rectangle;

import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import java.util.LinkedList;
import java.util.List;

import com.lib.udacity.simulator.Simulation;

public class ControlPanel1 extends JPanel implements ActionListener,  ChangeListener
{
	private static final long serialVersionUID = 1L;
	private Simulation simulation;

	private JButton btnStart;
	private JSlider speed;
	
	public ControlPanel1(Simulation s)
	{
		this.simulation = s;
		
		btnStart = new JButton("Pause");
		btnStart.addActionListener(this);

		speed = new JSlider(0,  100);
		speed.addChangeListener(this);
		speed.setValue(70);

		this.setLayout(new BorderLayout());
		this.add(btnStart, BorderLayout.EAST);
		this.add(speed, BorderLayout.CENTER);
	}

	@Override
	public void actionPerformed(ActionEvent arg0) 
	{
		if(arg0.getSource() == btnStart) {
			 if(simulation.isRunning())
			 {
				simulation.setRunning(false);
				btnStart.setText("Start");
			 }
			 else
			 {
				simulation.setRunning(true);
				if( simulation.start() )
					 btnStart.setText("Pause");
			 }

			 simulation.visual.revalidate();
	  	 simulation.visual.repaint();
		}
/*		else if(arg0.getSource() == btnClear) {
			 simulation.world.wallMap.rects = new LinkedList<Rectangle>();
			 int height = simulation.world.getHeight();
			 int width = simulation.world.getWidth();
			 int bgSpacing = simulation.world.getSpacint();
			 
			 simulation.world.wallMap.rects.add(new Rectangle(0, 0, width, bgSpacing));
			 simulation.world.wallMap.rects.add(new Rectangle(0, 0, bgSpacing, height));
			 simulation.world.wallMap.rects.add(new Rectangle(0, height-bgSpacing, width, bgSpacing));
			 simulation.world.wallMap.rects.add(new Rectangle(width-bgSpacing, 0, bgSpacing, height));
			 
			 simulation.visual.revalidate();
			 simulation.visual.repaint();
		}*/
	}

	@Override
	public void stateChanged(ChangeEvent arg0)
	{
		simulation.setTimeDelay(101 - speed.getValue());
	}
}
                                                                                                                                                                                                                                                                               src/com/udacity/simulator/view/ControlPanel2.java                                                   0000600 0000000 0000000 00000002555 11757604522 021111  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.view;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Rectangle;

import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;

import java.util.LinkedList;
import java.util.List;

import com.lib.udacity.simulator.Simulation;

public class ControlPanel2 extends JPanel implements ActionListener
{
	private static final long serialVersionUID = 1L;
	private Simulation simulation;

	private JButton btnGoal;
	private JTextField goalX;
	private JTextField goalY;
	
	public ControlPanel2(Simulation s)
	{
		this.simulation = s;
		
		btnGoal = new JButton("Change Goal");
		btnGoal.addActionListener(this);

	  goalX = new JTextField(35);
		goalX.setText("770");
		goalY = new JTextField(35);
		goalY.setText("570");

		this.setLayout(new BorderLayout());
		this.add(btnGoal, BorderLayout.EAST);
		this.add(goalX, BorderLayout.WEST);
    this.add(goalY,  BorderLayout.CENTER);
	}

	@Override
	public void actionPerformed(ActionEvent arg0) 
	{
		if(arg0.getSource() == btnGoal) {
			int x = Integer.parseInt(goalX.getText());
			int y = Integer.parseInt(goalY.getText());
		  System.out.print(x+" - "+y);

			simulation.setGoalX(x);
			simulation.setGoalY(y);
		}
	}
}
                                                                                                                                                   src/com/udacity/simulator/view/ControlPanel2.java~                                                  0000600 0000000 0000000 00000002551 11757604326 021305  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.view;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Rectangle;

import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;

import java.util.LinkedList;
import java.util.List;

import com.lib.udacity.simulator.Simulation;

public class ControlPanel2 extends JPanel implements ActionListener
{
	private static final long serialVersionUID = 1L;
	private Simulation simulation;

	private JButton btnGoal;
	private JTextField goalX;
	private JTextField goalY;
	
	public ControlPanel2(Simulation s)
	{
		this.simulation = s;
		
		btnGoal = new JButton("Change Goal");
		btnGoal.addActionListener(this);

	  goalX = new JTextField(35);
		goalX.setText(770);
		goalY = new JTextField(35);
		goalY.setText(570);

		this.setLayout(new BorderLayout());
		this.add(btnGoal, BorderLayout.EAST);
		this.add(goalX, BorderLayout.WEST);
    this.add(goalY,  BorderLayout.CENTER);
	}

	@Override
	public void actionPerformed(ActionEvent arg0) 
	{
		if(arg0.getSource() == btnGoal) {
			int x = Integer.parseInt(goalX.getText());
			int y = Integer.parseInt(goalY.getText());
		  System.out.print(x+" - "+y);

			simulation.setGoalX(x);
			simulation.setGoalY(y);
		}
	}
}
                                                                                                                                                       src/com/udacity/simulator/view/SimulationFrame.java                                                 0000600 0000000 0000000 00000001605 11753200560 021507  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.view;

import java.awt.BorderLayout;

import javax.swing.JFrame;

import com.lib.udacity.simulator.Simulation;

public class SimulationFrame extends JFrame
{
	private static final long serialVersionUID = 1L;
	
	private SimulationPanel simulationPanel;
	private ControlPanel1 controlPanel1;
	private ControlPanel2 controlPanel2;

	public SimulationFrame(Simulation s)
	{
		simulationPanel = new SimulationPanel(s);
		s.setPanel(simulationPanel);
		
		controlPanel1 = new ControlPanel1(s);
		controlPanel2 = new ControlPanel2(s);
		
		setLayout( new BorderLayout() );
		add(simulationPanel, BorderLayout.CENTER);
		add(controlPanel1, BorderLayout.NORTH);
		add(controlPanel2,  BorderLayout.SOUTH);
		
		setBounds(100, 100, s.getWorld().getWidth()+20, s.getWorld().getHeight()+80);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
                                                                                                                           src/com/udacity/simulator/view/SimulationPanel.java                                                 0000600 0000000 0000000 00000006222 11750200376 021516  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator.view;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;

import javax.swing.JPanel;

import com.lib.udacity.simulator.Simulation;
import com.lib.udacity.simulator.abstracts.SimulationObject;

public class SimulationPanel extends JPanel implements MouseListener
{
	private static final long serialVersionUID = 1L;
	private Simulation simulation;
	
	private int px;
	private int py;
	private int pbx;
	private int pby;
	
	public SimulationPanel(Simulation s)
	{
		this.simulation = s;
		addMouseListener(this);
	}
	
	@Override
	public void paint(Graphics g) 
	{
		super.paint(g);
		
		//if(simulation.isRunning())
		{
			Graphics2D g2d = (Graphics2D)g;
			for(SimulationObject o : simulation)
				o.onPaint(g2d);
				
			simulation.getListener().onPaint(g2d);
		}
	}

	public void mousePressed(MouseEvent e)
	{
		int bgSpacing = simulation.world.getSpacint();
		int height = simulation.world.getHeight();
		int width = simulation.world.getWidth();
	  
		px = e.getX();
		if(px < 0)
			 px = 0;
		else if(px > width)
			 px = width;
		
		py = e.getY();
		if(py < 0)
			 py = 0;
		else if(py > height)
			 py = height;
		
		pbx = (int)(px/bgSpacing);
		pby = (int)(py/bgSpacing);
	}
	
	public void mouseReleased(MouseEvent e)
	{
		int height = simulation.world.getHeight();
		int width = simulation.world.getWidth();
		int bgSpacing = simulation.world.getSpacint();
	  
		int cx = e.getX();
		if(cx < 0)
			 cx = 0;
		else if(cx > width)
			 cx = width - bgSpacing;
		
		int cy = e.getY();
		if(cy < 0)
			 cy = 0;
		else if(cy > height)
			 cy = height - bgSpacing;
		
		int cbx = (int)(cx/bgSpacing);
		int cby = (int)(cy/bgSpacing);
	  
		if(cbx > pbx)
			 if(cby > pby)
				 simulation.world.wallMap.rects.add(new Rectangle(pbx*bgSpacing, pby*bgSpacing, (cbx-pbx)*bgSpacing, (cby-pby)*bgSpacing));
			 else
				 simulation.world.wallMap.rects.add(new Rectangle(pbx*bgSpacing, cby*bgSpacing, (cbx-pbx)*bgSpacing, (pby-cby)*bgSpacing));
		else
			 if(cby > pby)
				 simulation.world.wallMap.rects.add(new Rectangle(cbx*bgSpacing, pby*bgSpacing, (pbx-cbx)*bgSpacing, (cby-pby)*bgSpacing));
			 else
				 simulation.world.wallMap.rects.add(new Rectangle(pbx*bgSpacing, cby*bgSpacing, (pbx-cbx)*bgSpacing, (pby-cby)*bgSpacing));
		this.revalidate();
		this.repaint();
	}
	
	public void mouseEntered(MouseEvent e)
	{
	  
	}
	
	public void mouseClicked(MouseEvent e)
	{
		int height = simulation.world.getHeight();
		int width = simulation.world.getWidth();
		int bgSpacing = simulation.world.getSpacint();
		
		int x = e.getX();
		if(x < 0)
			 x = 0;
		else if(x > width)
			 x = width - bgSpacing;
		
		int y = e.getY();
		if(y < 0)
			 y = 0;
		else if(y > height)
			 y = height - bgSpacing;
		
		int bx = (int)(x/bgSpacing);
		int by = (int)(y/bgSpacing);
				
		simulation.world.wallMap.rects.add(new Rectangle(bx*bgSpacing, by*bgSpacing, 10, 10));
		this.revalidate();
		this.repaint();
	}
	
	public void mouseExited(MouseEvent e)
	{
		
	}
}
                                                                                                                                                                                                                                                                                                                                                                              src/com/udacity/simulator/WallMap.java                                                              0000600 0000000 0000000 00000002215 11747751164 017007  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.LinkedList;
import java.util.List;

public class WallMap 
{
	public List<Rectangle> rects;
	
	public WallMap()
	{
		rects = new LinkedList<Rectangle>();
	}
	
	public void loadFromFile(File f) throws Exception
	{
		BufferedReader in = new BufferedReader(new FileReader(f));
	
		String line = null;
		while((line=in.readLine())!=null)
		{
			String[] args = line.split(",");
			switch(args[0].charAt(0))
			{
			case 'r':
				rects.add( new Rectangle(Integer.parseInt(args[1]),
						Integer.parseInt(args[2]),
						Integer.parseInt(args[3]),
						Integer.parseInt(args[4])));
				break;
			}
		}
	
		in.close();
	}
	
	public boolean isInsideWall(int x, int y)
	{
		for(Rectangle r : rects)
		{
			if(r.contains(x, y))
			{
				return true;
			}
		}
		return false;
	}
	
	public void paint(Graphics2D g)
	{
		g.setColor(Color.DARK_GRAY);
		for(Rectangle r : rects)
		{
			g.fill(r);
		}
	}
}
                                                                                                                                                                                                                                                                                                                                                                                   src/com/udacity/simulator/World.java                                                                0000600 0000000 0000000 00000006421 11750126210 016522  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.udacity.simulator;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.Properties;

import com.lib.udacity.simulator.abstracts.Background;
import com.lib.udacity.simulator.abstracts.Configurable;
import com.lib.udacity.simulator.abstracts.SimulationObject;
import com.lib.util.Random;

public class World implements Configurable, SimulationObject, Background
{	
	//Why not 1 global static object?
	private Random r;
	
	private int width;
	private int height;
	
	private int[][] background;
	private int bgSpacing;
	
	private BufferedImage bgImage;
	
	public WallMap wallMap;
	
	public World()
	{
		r = new Random();
		wallMap = new WallMap();
	}	
	
	public int getSpacint(){return bgSpacing;}
	public int getHeight(){return height;}	
	public int getWidth(){return width;}
	public boolean isInsideWall(int x, int y){ return wallMap.isInsideWall(x, y);}
	
	@Override
	public void loadProperties(Properties p) 
	{
		bgSpacing =  Integer.parseInt(p.getProperty("worldSpacing","5"));
		width = Integer.parseInt(p.getProperty("worldWidth","800"));
		height = Integer.parseInt(p.getProperty("worldHeight","600"));
		
		if( width%bgSpacing != 0 || height%bgSpacing != 0 )
			throw new IllegalArgumentException("Height/Width should be devidable by spacing!");
		
		background = new int[width][height];
		
		try
		{
		String mapFile = p.getProperty("mapFile", null);
		if(mapFile!=null)
			wallMap.loadFromFile(new File(mapFile.replace("\"", "")));
		}catch(Exception e)
		{
			System.err.println("Error loading Map File!");
			e.printStackTrace();
		}
	}
	private void bufferBackground()
	{
		bgImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
		Graphics g = bgImage.createGraphics();
		for( int x = 0; x <= width; x+=bgSpacing)
		{
			g.setColor(Color.black);
			g.drawLine(x, 0, x, height);
			for( int y = 0; y < height; y+=bgSpacing)
			{
				g.setColor(Color.black);
				g.drawLine(0, y, width, y);
				
				if(getColorAtPixel(x, y)==0)
					g.setColor(Color.white);
				else
					g.setColor(Color.gray);

				g.fillRect(x+1, y, bgSpacing-1, bgSpacing);
				
			}
		}
		g.setColor(Color.black);
		g.drawLine(width-1, 0, width-1, height-1);
		g.drawLine(0, height-1, width-1, height-1);
		
		g.dispose();
	}
	
	private void randomBackground()
	{
		for( int x = 0; x < width; x++)
		{
			for( int y = 0; y < height; y++)
			{
				background[x][y] = r.nextInt(2);
			}
		}
	}

	@Override
	public void onPaint(Graphics2D g) 
	{
		g.drawImage(bgImage, 0, 0, null);
		wallMap.paint(g);
	}

	@Override
	public void init() 
	{
		randomBackground();
		bufferBackground();
	}

	@Override
	public void update(float dt) 
	{
		
	}

	@Override
	public int getColorAt( int x, int y )
	{
		if( x >= background.length || x < 0 ||
				y < 0 || y >= background[0].length )
			return -1;
			
		return background[x][y];
	}
	
	@Override
	public int getColorAtPixel(float x, float y) 
	{
		int bx = (int)(x/bgSpacing);
		int by = (int)(y/bgSpacing);
		
		if(bx >= background.length || bx < 0 ||
				by < 0 || by >= background[0].length )
			return -1;

		return(background[bx][by]);
	}
}
                                                                                                                                                                                                                                               src/com/util/                                                                                       0000700 0000000 0000000 00000000000 11762166563 012101  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/com/util/Random.java                                                                            0000600 0000000 0000000 00000000563 11743745430 014165  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.util;

public class Random extends java.util.Random
{
	private static final long serialVersionUID = -2440064819342501060L;

	public synchronized double nextGaussian(float m) 
	{
		return(nextGaussian() + m);
	};
	
	public synchronized double nextGaussian(float m, float s) 
	{
		if(s==0.f) return m;
		return(nextGaussian()*s + m);
	};
}
                                                                                                                                             src/com/util/Random.java~                                                                           0000600 0000000 0000000 00000000563 11743745430 014363  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   package com.lib.util;

public class Random extends java.util.Random
{
	private static final long serialVersionUID = -2440064819342501060L;

	public synchronized double nextGaussian(float m) 
	{
		return(nextGaussian() + m);
	};
	
	public synchronized double nextGaussian(float m, float s) 
	{
		if(s==0.f) return m;
		return(nextGaussian()*s + m);
	};
}
                                                                                                                                             src/lib/                                                                                            0000700 0000000 0000000 00000000000 11762166564 011115  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   src/lib/MyProject-20120525.jar                                                                      0000600 0000000 0000000 00000115672 11757604526 014442  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   PK
    �N�@            	  META-INF/��  PK
   �N�@W���^   j      META-INF/MANIFEST.MF�M��LK-.�K-*��ϳR0�3��r�Cq,HL�HU �%-�x���RKRSt�*A���⍌u���4�K�|3���+�KRs�<��4y�x� PK
    ��@               com/PK
     n�@               com/controller/PK
    ��@               com/lib/PK
    ��@               com/lib/controller/PK
    ��@               com/lib/udacity/PK
     ��@               com/lib/udacity/simulator/PK
    ��@            $   com/lib/udacity/simulator/abstracts/PK
    ���@               com/lib/udacity/simulator/view/PK
    ��@               com/lib/util/PK
    �o@               com/udacity/PK
    �M�@               com/udacity/simulator/PK
    ln�@                com/udacity/simulator/abstracts/PK
    �N�@               com/udacity/simulator/view/PK
    wn�@            	   com/util/PK
    �N�@               lib/PK
   �m�@Ȍ���   �     com/controller/D.java}��j�0��1�����
=8Оr�(ҺVd!�L��ݫ�
:���ov�T�|CP�MXsjvfk1�XǺ��G蔑�o�H�%�O��_\�pЯe��:���(PV�����n}F�1��u;�"	a��$�t��x��dmZ�[��ߝ{�ӂ�Ŕ��q_6w�n���I��W�?]�h�P��Ω+U�F]�MX��4�M��PkI�U������j�?z��n{kp��F41�H�+4�oPK
   �m�@��c  �     com/controller/Element.java}��r� DkkF�p]b��I�"m��?�a3A�A�O�=�Dr5;�v�:�x&���nj�,{g���(�.4FЖ�+/�Z�eq-�ݡ��	����À&8|��O��=�Q�Iy���ό��ӤGer�ݜ�F��A�G33p&���W0�� #p�2�r>:�L�<�C�����dx�--�q| ���Ȏ��[�06Ǘ�'~*{����Zyc�!��o(XqA{&Y/����%}ec�}[�[���F�	1��*�oPK
   �m�@.)�L�      !   com/controller/ElementHelper.java}P��0>C�;�❘x1��3�Q�bٖR��]�2Ѡ�~��J��A��"�T�YaG�\y��fVZ@�8�h����>��C�ߋ<���`9%0)������X?�r�cCF��<�bٽ0�Q���v&?6�1ˎ�	�M�|r��a��VN���G�r�2��6�7�!@xG�^���74���o�(�
�I��	PK
   �m�@�<�P�   E     com/controller/I.javaE�Mj�0����L\P�/�n
�gP�q*<��42�һwd'f�~��$�f{Gp�a�ߌ��s$����V���
z�=[�O�6+��p٭8����I�To�8��� ����\�f�~��R��e���e��@�f����f8��#��j]��8��-��/f�ξ	[��k����;j�4��:�N],U������.�^�JF�9��y���PK
   �m�@6|eq�   �      com/controller/Link.javaEN�
�0=[�?�t�1�a���Z�Q�m����}�	B�{///;��cC�kl���VZ�u��pq	r~h���N2˰�V1w�,X2�w��}?��pD�7��I��V�&^de,`1e��J>_i��cƔ\��ѓ�aȱ7���y7�e�pk�ũH�9yX��Z�PK
    n�@װ.��   @     com/controller/P.javaU���� �s�a�m�������5�`ʹ+���c(��{5i)�0���&�&{Ap�jȟ��A8!��j��ZA�Y|�����A̒�"�|�m�aJm��*�y�l�0 �Ø��_����]�.��� �)Z�@���\еpe��;�B��Z�K%6�m;�ɟ�f�N�k��8#��C�PIc���QgK�}h��p�%}�u=PK
   �m�@p�&C  a     com/controller/PT1.java�R�k�0>+�?�c��s)���v�y���&$O���K�T������{߯5�?��V�b�jՓQR��di�VE��P��0�@�H~�g���@z ؂����u����]�yU��a/E�����n�Ӂl�*Y����6b��J�	�抵�k@txSmk�&Ӡ�$ƛ����x��R/��k���	�eފ��O�z�����A7�'�4��$��,����$���r�\�b�Z(!�䯜���۵��(�Oi0}�r?بD�b,�/�_Ī������	�vn�4������.���Ev��e�{
�V����G��_�W�r�/PK
   �m�@	�:y+  �     com/controller/PT2.java��Mj�0��1��t�q����M�-4��I:T��~�E��+UJ�Ҧ���|�f���;?!jj�͠�3J4]Y��~�+��+ceF4 ���ޓ�w����Hƺŷ@,B�D��,��0n-�ФN(����(�ϲ�hC3wjZЮ�~I,JQM����Bq����b�Pi�������C����*�V�7�W�{# u�����������rg�趰�bI�]�5�,�t�72�����7+!�4��im��;83��ڮ/�$�^��C8�_��1R�j�e��9i���e�%|_PK
   �N�@qt��3  �     com/lib/controller/D.classm��N�@�϶��X���R��M���Ĩ�'�aM�KK���HL $^� >�q����왝9������We8h�P��q�8�3�9�qYD��@�x	��@A>�6���t��}������h��u���ρNIZa4M���t�.�p��¨3�5<��ǲ!��IO���a%�Xk5�=
�v�����(yVz�f�/ Z4,�U�hC��URAVԥ����Ôm�}�?���k��@��ƘP��|/aIVܻ�5�[���f>ɑ�l�73��U)
��\�8�o<j���{�vg{i}�PK
   �N�@]���   �       com/lib/controller/Element.class-�;�0��O���$�%�@Z:z�X(ыEvG�8�1l3�)��y� �qP�)�D�x�67�mݴ2Mw���/C)ߓ����6�8"7����\8f1���k78%���ip�PJ�����_PK
   �N�@)�=o�   �  &   com/lib/controller/ElementHelper.classuOMK�@���6ij?����\<�1x��=���l���,AP���(qc���a�ݙyo�?_� �q��0������D�Tb*�or��"c]V�u+ܔU��
x���tW?S��lC�bDĐ���H�z�L9WE]�Mm�nԽ�K]�ڬt#0Z�\��zQ��.8����K����'�#�Fx�O��%T8�i�	��?�Xp�KVo�Ǫ���ZA���r;�b�� ���}L�A~��{�w��A��g�/PK
   �N�@Fb�#  �     com/lib/controller/I.classm��J�P��M�Ķ�ֶ�T�U�P�&�Z����?w�z����X�BK���C�3I�M���3s��_�� nЯ���*�8d1�Y�2N����3��[  ��mɝ@e0�~��M��b:JT.Ә��40Y�>ҩr����:\F+G��`��ht&����؟DaGZ���(����0yRz�b\�?j�C:��PfSNk�{T�H7(6e}!��#�����~1y�J6ٕ�k�r�
=c��ƛ�4��h��������%���ۿ�[�n[z[ث��)�;˿v�}'??PK
   �N�@�D�  �     com/lib/controller/Link.classm��J�@���մ�M��(n�l�E1�p����N��PP]�|(�4����;��?sf��7[ 7������=2��<f�'���Sg�m�&址>���BR����cOc3I�lL�I^�}�*����.����c��y��T�ͳ�,2�d='��e���R��T�,D�+��>-�]�h�Q7����!0�~��I�(���'t
��]�=?����3�a����-Z�庆�n��s�Z�ʝ����PK
   �N�@�g8  �     com/lib/controller/P.classm��J�P��ͯMc�i��U��M��"�����.��I(��U(X.| J�I�n���̜9������p�3�Zha�q�8d�q�8a�\������	8�I�7�pt�D�.�*��|:.�Z&���yY�úz�R��F�G�����.��e���&�,��s<��b�i������^��J��s5��ã����2�rZKܡ�G�A1��
B�W0䀰� ����v�R�äg��`Q�ln����3��-+���ߥa�ԑ�
β�G���_{����R� PK
   �N�@\�3��  �     com/lib/controller/PT1.classm��N�P��[���T����e!ѥ1n��.��Kho��BSi�K��$&&5>�e�)X]H�w`�3�_� ���E�c�Qb,1�+Y�b�����"��&0�m)�G�杤�xWn�����ݠǽC?��#:[�U�H���{��ˤLI�vz��V�5X&&`��d�S�<L[&�Q(֣���S�¸��:�{���w��o�s�%�[���i �2L��f�_י�RY�wx���	6�7d ���W�ߦ�vCͥ:�j~�:�/`�8Co�R�~��'^�0T�Cc�E�g�%0���|@al޵�P-�����h&A�����c��q� �S��-Q�:�)%��n5y��[���őg+�,$���~ ��h�|�(�
R���Q�Hq���|����7PK
   �N�@ʀ��l  �     com/lib/controller/PT2.classu��N�@ƿ-�忀�"��KW�#'=�SR
!��21ђh��Pƙ����73�����?��� :0�H�@�a
�	�8b9N���^�唥��`9�p��BCS 2�����xd�N��=:v]{j><�/C�#�r<ǿ�6��VO@�?��a�M�-_�]�o2�)�-wFۑf��#��@q�M|Zб���K9E��(�Ay).+�M!��5�L��^��������ֵG���z��k� �K���z[�mP�h����jAE�b�X@_P��D>��y#̣o���
�-GM
3���V ��(��R�� q.9}����B�HH:�Z^#U�d$����"�<EA1�0@rs�6B��$�PK
   �N�@��dX�  �  ,   com/lib/udacity/simulator/BicycleModel.classE�MO�@�ߵ�u>�%�BI�J*!K=�PAո�E��"Nkc�Ǯ�S�)7=�T�֞@����sb6u���g�]�;�n.x�Z	e<*a�����ϷkEOT��R��� �%�:��l�Ao��r��Ч�$)C����.���LzÞ��'��7ab��3�X1��&���+�^2����Ƈ��S+F�Hfɉ�6�N����W�B(?I+��톾�1��o�d���e2&s-��H7U�m�%=h�{I���*40��<�C��j��9؏���X�_����6��6����.���0B�(��'��>cWpa�v��$5��Rxd�
�m�rS������GΌ*(��w_Q�ODa2{>����=q"�_�^�r�� ��'���Q���5M[nPK
   �N�@(o�L�   �   ,   com/lib/udacity/simulator/DefaultCar$1.class��A
�0D�W%��.�m�+T.�3�����	4���\x %F��3��0�^�����L ',NY�kO:^}#0'l��5�V&�e0�h9�A���G+�[��sz�,������Ҳk���?�r�X~�0I=MDJ�>��2� PK
   �N�@��wIN  -  ?   com/lib/udacity/simulator/DefaultCar$DefaultCarController.class�T�n�P=/I�$ui�<$� ;�K'J� $TE��Ջ�()n\�.Rw��[v�J�V���Bܛ84B��zq|��7]����?����	�7R�H
��3b��J7n1�f0Le�&�����3FZΦa7��vCZM��۶�ר��r��+ҝ#�|���
�p��3�X�i(�ĺ�W��jD󅚀F�w\�J޿R,_c���/�׏��SY�U��ri${�xL-��u|�[��0) �A��܊-=Om%�RC�reڒ�S�q��4L����;s�Xб��Gw9Zf��Y��PS��廎m���No�7Ұek�x\�P�/P>zY�|WZ�g�g3��WHהCHI�R��i�uj�2��xo2f�	CZ�z='{m&ئ�L�V�{���5������47}�	D�'h�4eg(��;U,}C����.�T9p�+XY���>b���Q��.���D��f�w�Ы�0����@<��,��j�H<�m�/��OR|��VI�Jbu	�����~�עU��Z��+_�}\9j�흦A'�Z\���bi�{�׃�U��!��{�_��PK
   �N�@}UA>�	  �  *   com/lib/udacity/simulator/DefaultCar.class�W	x���%kW�����0 ˀ��LL �\l.���ҵ�62�J��$iB��!�iڦM�����bB��G��wz��}�7�BgV��l�W}�fޜo�{3��>��'Ԉ5~��g�'|��c>���>���8ɣ�1x��)��k��>�]�\jtF�P %fbD�� &��ϱ�'d�����'e|*��x*�O�3��Y}N����3~<��d|>������
�e|�G_e�_c�_��&�o��n�j{���.1�m��2�bG��2�+�{|?�������������������_��_��5����-������?�0d�QƟ$�9�M���h�I`�&��~��d�_��R�2�o?.�%���[��0��]�`�\��\�$!$�'	�$�PZt]3�ij�@i�֣ĭ�hH薑��5C@��FK�ګ	���ԈzЊ؜:b�IM�n�t3a4F�D�@Q�!#1�0-M�l�r�:�δ3d=R1T�;��막�C���Z{�=	�Z���H<��b��v[��	D�_�Q�V�1�PČ��U+aD�.�2ԨeFF��\�A��jX7��NwP/���q�*�LE===Qf�HS\��t���R+R�53f�f�!����%n���Z��}�cz�Z#�	U�$nC������צ&;Ԯ����IثqԤٜ"(r�P}*f:��Ԍ�4�>����k�|�nբi��f�tB<�vo5IͰb�cSB���-#�ce)�oUc�%09�I������5����w�Z�F5Ӭ����]'�LR�񎸆K��%j�k���Ҝ�fi��e��%�gKVd+����j�c��A$f�`p�{���ոOA�����30�O`�xR���ɽ�W0�%9jL�	K>�$P"���U���+	Y~ �}t�D�9�	W����$�(�PLP�1�T�M��*�4ՒV,�+��Ib�"���2�!1��X�8�f���Te�@���w�ILRD9�W�*ܡ��b�"�⸂�4ILW�1S7�i��ţ�b&/W5گnfՒ�����B�1_,�憱���ͳZ\��Ρ�nK7:�JU�߶M�Og�!>�4�S���(tv1+���EO��.�T��T/^N�Nq�F���mjk�N���9��1=Eڡ���t�ktuJ"��*�P��bEDx�(�F,W�
�R�b�"nu�XML�CsV�'Q�ɤǖ�>-J`�8ۓ@��4zO�w��N*0\��D`�8{Ƹ�*���۲}'�>S�,�fR�-âl"�횙0���P�Q�e���:Ǐ�Y��[�IY.%�����T�t�S��|�껆�R�.v̜�v�r*�&��==�j���5pg��EI�Ų��:m������r�r�_n,[S6#�Jr��z��u��׾��>��hVE���i�T��57W6���+u��=0![�ʯ����P#+{(��1by�	~c��R������q6�<�l֨�h�>�7eR5L�!r�:-��=�{�,Ty��[箓��8�3���M�^���Te���RIh��S�g$,{2_����9�i��ޭqX�hc�75u����R��R�޲y�$n��ܤ�6�h��Y�)���z�1c�g�fb���%�#��'˅@M�ޯ����w�A筼44����26�m��.S3��r7%iw�L&L��v��1�> T�QL&L7)����Y`㸃��;8�ः�;�p0]�6�������9�V����L׭��t�a����v�=��ƥ�-B���!j�$��G��� ��>�p�h����!��Q�#(B�:GP>���aL	Nƴg1���;�3F0�,n¬(	��g1�f�Vc�iT�c>ϳ���L�2Hߑ�����^�!�u@�z	�WHr�;��H����>�I��L�hNq�+~ �X��7�œq�ġs���9�S'<J�xS�i�w��xJ,N����p�,��EA��/~�Qlf���L�������9,������x�T
RnCs�aQv���0���L����N�f��!�mA%Ő�.����c�i��}��r/�A}^_m~y�YD�����G�����Z��?��+�����2��Rfu���r���.W���.�3\[�g�L]^)���8�%��-�u��c<U��f睲�����P��%�(��,"�Cx�s~S���T/���+�+�Q{�����7fH�ȺYH��9�ț2���5�K���:��'r}�l �1��Ddsp�K�1������\ݦ�J0��M�#hB�ErmTӛ��
n��nh�n(�e~x/ᙼ�� 1�[�*��Ҝ�i��֧��m�ilF�B{�K����>�a�$�Ӹy��0˖�bw��|y�1�[v-�+N9��tk�A�������9�'3�(!�
"\������)��x��2ކGrԴ��#~{N��߁Gq	��^)<w�$W�9�}��]װ�wޝ���ߓS�q���)�s���)N���S)�n�2Y��p/�X�b���_PK
   �N�@�E  �  +   com/lib/udacity/simulator/SensorArray.class�U�wU��f�I�B1�@]J�P�bE,�F-��X�N���3qf�����*�UQ�]P���/~��'���G�ޙICe9sN�{w��n���ЊcX����	w3�3��A?�{ܧ�����Q,�B�a��Уh�by[c���(�EaD�=�Pb0� �r�fs�
W�HWcb�S�.��0�a���|\��y�u��(�f���趻��9�=Ϸ��"�^R�G��*^�@��`������(���̢5�!0u���tӱ쵖��$��VІu[�kCz@�'����HV@�"U�����nWq��g�5
1�)i�a�͵p�Z�pw�\�n�M�Q|�e�i���ĥ�$7	(]V��N-YZ�϶ʺ��#pU�g��C�SPcx:S�t���l�p"��O/��s��k��m���xU�^_<�q��REG|Zw_��r��
��t��٧�+pe�����mk�mF�i]����%��yT��&�.l�X�[%�t`��r�V`�����W��H���T�E*^�xo�xS�-��[�H�m�#p�DT+�X���M.����^mU�+�$�����0*�!F)M�c��%_������mmW����O$>�!��p��xB%�ޒ5]}H�%>�_�+��q��D����
\��s�|��wl��J��)�?H��O�1�1T$� Y8�k�6��/�a^r��i>j{���ے�j��kk�9�M�j.E�K����-�T�L����+�B_�8+]9�6̡�s)�sI�#5Z�&����5��$~�I���'�5/$Bm1�R&���Q�E:���2��8�;JjA�����'D

)��b�G�< ��*Q�}�N���!����M}��@Idy|c��d��'����dM�(꛵����&�հC+��[f��y:���b�?�󻧃(��0f�<��$�e��Ď(��[qC3�G�򛄇Q��h���֊S�%gm�O�b�LڞS���L!S�4�L���`��:��-��ͨG/:��������U�˃�38W�m�I;��(���*��	[�q��R�!Rc�cJ�Ơ03�0PS?!�?��1�R�14�2��A���ҍ�qJSO�26�n�VCC�Nol���&�xy��Bg�P��V[�T�Jn���14TpE�^���8��A�,�
fw#V�Igh�Q�7)���)4�C��X>�ԛ;♿���8��*�R�C�ޡ�K1ar
���Γ5��ێ㚪�
�]�4�������༈��)�-���{�#����4���\����S�KA������Y����𜁶��3ǚ�t>�7]���h�[jS�
��xa\i��J~A"�ZA��i�M�h�q���ky��4�X+�?h�o��ѿ�RE���S��'(H���i?� 1�t�� ���4�FʄOF�y����uG�"��������V�V#1�^�������w�%�?��2@B��J� f�Aސ�`�8n�C�O浌c�/2��x�u8:��0Bͳg�PK
   �N�@�sa��  �  *   com/lib/udacity/simulator/Simulation.class�Wi{U~o�v��Xh)K[�ZR0j]*hH1-H�P\��P�3q2)�}Cq�p��.���P���������Q�Y�c-��ޛs�}Ϲ�s������QF2��rx�J��$�$l�!aH�M2*��p��(2Q܂[��6n�����.���	;dLǽ<�'a��Yr���x�<�HE�0��Q	�E�8��b��b���i<#س<얱�EZ_�If��l����/��W$�*�,��Bs�KxC�%�%N����D��z_<�R��3��YCu,;��e[M:�x�j/(�f�FJ�q�=�لl�v�*=�h�F�M�Y�'�-3��$�JGЖk�:D�'%����N�f[S)���uP����dp����W�|P�dUC��	Եm1�UM� ,��ۢQxS=WYG7�!G׭�����5�UǨ[���k\?K�l���Rح��;K)�M�"i��"?��s�w>�w����.����	g�������~�G�S'�P J��_<Ig%o_!��qD3��K�N�#ֺ�i�f?'k#�*�L^D����e�@�D�J��!�L�	�2�j;D�nGMn�T�=j�A�*��j��M:���T@�nǦx�ꇄ��t����f/TJޑ�.}���h6�"0�2>N�_N��*��<�hM>E킐}�	g�Z(s����+�	�A��X&P[��[�_����L��wҭ�˾Զ�!��+pڿ/�6�Y�����[����p��E�HA�)h�+X�
.��T]��c�>)$�N�ֶҚ��U�W�[񕺡��=�ͻ��Ǉ
LX��#'pމ�Z�8�`		��ᰄO���
��u
��>S�9�P�%�R�5�����o�������/ �I��iGK�)��6]�%��x�E����Rļ"a@�@X�=�\��.�Yie�����5��Շ�ݪPU�*�ڨ��1��s�B3�J}KnO�A��GW)mV3]�v����T�B�'�����V�~�Xה(�Q/H�gN��Pu�Ne��mW��'߰Ʒ��.8�� �ir���ߤ��Q�﷙Pnj
��=D���u�NݠW�یVS���+�)�Ѹa����Y��Y�ך���Vu��E��A��=����ii�_��S��|�W�P��=ق����qa�g���Fs���;Sqsg���L%Ν�����,�����FӯU�ګ]�i$�Oc'�ڊ0�́�c b�B���9�cc��@Y�c�zI[�C%���1DiV�b�|�(N
a=/�/����bs��pC���q5͂�2����W�-���W`����#�h.���aj��]Z_�{pe	��}��*�/���7����&Po,{8��j\�ؚs��bk�_*�P��fP>���+?-8z�tj>��o!>0|=���,b�t��9Բh3#{�c	h4�!��r�	��#�2���a�s�f�6���ev��db1�^`7�h� ���[���C>�����*��D�����Q�-<��
�,�|���5��D��}%�}_3�_���A�~ekf�(N���ia�"#8=6�3��|��oq�%lX�4��!����N�f1>��d9�[T�4�foZ@h�w��P��EH�p]G>����
=ӟN/��V��J7sfW��Yw�P;�M������Ŀ�>Id/Գ<�z� �
ܘO\�kI��|�sBx���PK
   �N�@�>�ķ  @  '   com/lib/udacity/simulator/WallMap.classmT�VU�v2a'�P9[Zj��6!���� �B��$��P�n��3qf��M��\��.MD�ry�O���B��9�b�}������@
U��s��" =�)�Ƒ�x]� �PR���*���R��H���{*�0?��x_�,�ݝA,bI���u9�|�"�{R��X��2�\��{ë;�k��|��WM�O3D
�-��k0�8�<�:�o|=O��m�y2�3mӟgFc�0(�N��5��e��[6-:�D[榣ˋ��*�����5�iM�9����%�ꛎ�q|H�L/c{f�X�E��Ll��#�V�i��=t+��V̒�Z�(����i.��Q��4\�4�d؝�֖��!ʆ�0zq�R��.E^Ck,A�5|���O;F}Y�(j��Ci�����#_��M"����[��h0�ñ���L���-sS��E����=s�f	�qu�J$�ޢ����B�wU�]��f{�z��
9ֻ��C����o�2����JL��a���_��x4v^��W�L�t3���ع�J�.������z:�7�e��U�zFF6��y�3�z���@^�okj[Q.�1l�.� �%��P�쒟�p�K
a����~s�V����\�}�ǒc�Ծ^�l�Eǒ!"K���V���v_���ovr�~�~,z֨9�[���ӏ����i��~.�o�ZZ��+t
�(��!"9C7���m��"Pl �3�g@��E\'+����g�:D�x��b��@8�r�:"��XK��u�R��`*X����7� .}#�?A9�PqJQR��j-��˥��0������y�Y��K$'���Q��9n#�q�� ��$Y��E��,K�$^]�<�(C.y�1�'�B�q��1$�^��c�	B������O��4��r$�Q
�x����Z��1Y����D;�D�!O�qq����A�1B��d��PK
   �N�@��R��  �  %   com/lib/udacity/simulator/World.class�V�g~�����tB`!��n�5��,�-E�$���H$H���ٝ�f`vg;3K��*�*^��[�/x	6,J��~������93�I
����ﹼ�<��ٿ��� �GpZ��"��I�C^FAE"$^L^fx)�`V�������U�PV�(�(xJ�+�S�؂��C|眂9��+������*�E�-}B�'��>��i��gU�qA��T<��|�>=������E^�������
/_e��xy�c���o��l�[��m^�#�y�e,�����	W�u�������V}���ˆSH�Y�?K:9��Y�*��j^/�-�N�l�O�"Y2_����\���\I/�;������>�g-�d��33�k����s�m���]k ���g=�T�u�q�S��7�ʖ?D^3='�� 7j��C�~ a<�:�U�<��Y^��Y��&)�L.����э	ש��o����L�<Hƚ`��6O�>�9��m��&�1�5���'�dqx]�d�<�0�2k�y��+�V�88�8F��Z1t�2���(G�q�r��e�9a�7��FG{r�Q����a��o�5���aix������(�s�k������W4���@%�{|��=��zY����3Ȃ���ٜm�E�>��%��9_0+����;��Zڛu���Λi�<g\�t~>�h�8�kxQ�KzeԲ)�Z��r�!)v
@�O4,�~��S�֠����W�K�mG\�q��)�%M�I��.���k���x�[u<C[�0����2^Ұ�u��\��;���#xR��4���?0�&�jx��'�_4��k8������('g��q-�c�3f�J���/�y�w���eG��U���g���ΕɐG��{��v��)��z[�Ij+z=/�?zXA���K����s7��3�ŲoM�JEw=3�O���e~��'ߐ�K��[/P��42����SU�\0ߌ����8�:���7EV�>�Ƽ�%zz�����Y�ɦ����܀M�+L��[*!��u��i�i�c_
��k%ۖ�i8�Hu��/\y��Y�;�F	�*^4�\�N1�UW��ʄEf,��ܬ�Ϣ�Sc(3�m�Q6,��x�]6��Au�L0P77@K��}�\� ���rw~����g��LBH��D��>����؏w��4�b<���G��k�?�4��}8�ih�.x&��L'����&�4��޻�{��ė!�1AǦe�K@p��x_ti�|)�����x��8Y�7�u1}"�VB�]%���Q�=u�	| ҹ��@�޾��j�a�u�,C!rcjS�T�L�6��$�cĕ�hah��y4����T�
����$_Ŷ�2��R�]���3��w�?՞"T�+�Q�}��8~]��5����%B�$���&p�0jH�G�{�eLjT����7E!��J��u��
ޱ�n:vא��`ɋ������޾�8s�5�Ň:�t�uY�j'�z;.v^���2�I�N.B�����t��െl@�Z����.޾T��%#nB��������,���[��:v���x�bw�-��B��pr5	��.����v�u=a�缭}�))Q��cbb���.Z���e#��#Iq���?���tc,Hw<N��b��=���5��$=����p]�	��T��WE���C�p$:5o7��v�
��/ ձ�D[|��HĮFq�����X;�/xdj�%��.�������>�3��ֹ�-��ZZ�;�w�J�(����BPl�PK
   �N�@]���   �   4   com/lib/udacity/simulator/abstracts/Background.classE�K
�0��sk�D���@�BG��۴�Դ��Ftk\����3��;���`�E������Z99��A.��ZB�)�mEX���Uq�ݠ��UhXy����8���ĳ�IY_;����=�XY;u��VKN $�KR�)�k�<�PK
   �N�@E�   D  -   com/lib/udacity/simulator/abstracts/Car.class���
�0�g��_շP����$'��EǴ�%6�F�Ws�|(1Ҁ�����o�{�O ��È�Υ=��|�4'B�aS�J6�`�4>^��������J}W��|��3WE¯�H{�uq�*a��"����y,�O[�J�I)n�+Q�|��2���?��j��@h�
�'¶;�1�d�]Ϟgg�PK
   �N�@�62ؘ   �   7   com/lib/udacity/simulator/abstracts/CarController.class=�A
�0D'���Ѯ�^�P�.�iJK�H�+�j.<��S)��3���|8a/��1����ݘ�a��%���y�.V�_��oKB�x��v��m%�Z�&�~�����
䕦 �7�w�ΛC�JZ54�RuFS����,���h6�ә�PK
   �N�@��*�   �   6   com/lib/udacity/simulator/abstracts/Configurable.classE�1
1E���vb��������d��n$�^��x(ѵ�W��z?� 6�kLjL	��9�xuI�˄�r��pQ�/��amc��.�X�wξ+A4&�5��̻؟}[����_,H���\���'a�aTƨ� PK
   �N�@�Ό �   q  <   com/lib/udacity/simulator/abstracts/SimulationListener.class��MN�0��!MZ~��ae�6��
)�"�d5qLqIƕ〸���� �ͧy���}�|~X`��"��@d�x��4W����d_�2�Cv����I�:�H�Nf�2��٦�ny�����ٞ��������&����jT&�כb`Z��/2j�#�8-��QK,o��P�*�w�F�޽\;ڿ�-�B��r��Y;��C�������`���x+��V>8�8q$p�8A�`8�I�)����PK
   �N�@>~Qj�   �   :   com/lib/udacity/simulator/abstracts/SimulationObject.class���
�@����K!V'bg�h#(��Kԕx'�E��,| J<{�eؙ�c���ёhJ�$�U6�����SB.�n4{�Қ��y/Z�L�.N�s:�Y���}4���2�U��fwUˌ��Ņ�I�B��[������٩�5��4�f˻2�8KC�����T}o� �!�G�h�/PK
   a��@�K���  �  1   com/lib/udacity/simulator/view/ControlPanel.class�T�rU��I��u+!��EZ��I*,��DiZ45�HJ5Uԛ��lv��ݔ>
/�3C�3:��P�즁�`fr��s�{�������p;&pi
��X�'>5��g��9K�u\1a��\e�K^��q��4.��^6P�}��������7��f�[�R��)Z�3qu^�g?7��б�㖎M?hȇ2p��)���[�ښ���JxjS���!�i���E�P��n���l�i�QG��k�~`7F�����JJ�lm[�};�q����)�@ra_��s���td@��+�稫Jŗc-mj�V���pL�YU��?�1�B1��Ŏ��@zʾ�@VYN�NS��{뢿!Z.���JV�
�����L}����Ga�IS�u��qM%�-l᧣����޷p�X��Q�FI,��jb׏��%�*B�۠p'+�t�tuܵ�`��=�G�=��c�����-�AȋBda��K��?p�MWG�[�$߅C���_X��*��@Ùq�}
��K��>�d�* |ҽ��9�tqL���\�Z=pp������a�2��A1�6E��7N=F�[���f�7��#L���}���3��hm�vzQ��_d"�J��M��(����᝗�&��7#ϣē�o�S �H�-nq0:�6�}������	#A=��c�ܛ�l�-�����R ��&�b	d_8\�;j�^�a�0��\����[��.`gH�b�xTz�&p��4��L��4��gs�i���A�,���>���&�#�,d����d��c�4��|gS{0Ik�����cXd�n�����|���q�%�P �a�
�>����i�K1f����6���d)c6q�Z��b�u�TG��)[I���s#��Ä�"�9dJs3��!>��S������8c�ىq:�O PK
   �N�@�hNK�  �  2   com/lib/udacity/simulator/view/ControlPanel1.class�T�rU��I�麕�R�"-V�M
,��DiZ45�HJ5Uԛ��lv��ݔ>
/�3C�3:��P��즁�`fr��s�{�����?��2v,���񡎏���@����,]�q�@���:K����q� �r�W�X5p_�
U^�������c}��o�B��o��m64tl踣cS�w
��n� t|�NuE���a��{���n$sH�#tz�+�5�[k�=�uZv�mG��C�؍|Ky%�a��-��8^�^[��J ��/e�9{�u:2 ��5�s�u%��XK���#5mV�ep�z̲`%4��Q�HO�7�*���i���`]�7D�%&�C��}�u���u(��Gj=�a�<�7�,3/H�r��(��k�(�lb?�`Џ&�p��]�d�g�B�%�����]?R&Z���In��PL2�Al���q߄�m�RIoL�8��>�:~5p!/
����_��#wl�:*�ݺ�{IC�P6�V��V��Jz2�pf\q�B2�iv�H��vC�O�w\t:G�.�i�"9����G)ώo�!�P��CM�oS�I����3a��u���l�x�K>�T�^���N=��ֶl�7un�M&�T?
��	�����8�''�y%��~���F������ېt:�'�����mrq��%��B���NPH�U�%�}�p��QC(�*O3����t�.ޢ�t8CRsX�۠�Ћ7����Nd�d�)�=C��@�M_rd������0Q��f1���&�O�C'e��)t�1���i_�p3�I���>^�q��G���Y2�E���0.�Ґ�O�L�\�1�'~C���'�$K�����b���˦:B���H�J��oĘI�'��i�!S��������}����E�$���N��i��PK
   �N�@8�1�  �  2   com/lib/udacity/simulator/view/ControlPanel2.class�U{SW�] �n
F�XQ�A\�U�*V"�� �A4}��$���ٍ�7<�?���)K����+u��sw4t���ssϹ畿���O W�Q���y�����[�q[��(nJ�]:>U�{:��&�6�u�h�5Џ��t|�hAǼ�����,b�_�K%C
>�e]Q�#�Q6��V�7���D�w��m�?�=�a�>�gH�=7�ܕ+�i��c0��r�$0Åb�kX�]�Z5^�喕�z�U���b�*ҝ��0X\��|�
6l�n�O����:?f8��|Yl�Y[8�]H������r�a,�n��Vz�^M0��-	����p&Y����ĺp�u/��(>RM�$�>[��e^q�II���8.2���C��ܭ��`��&&p�DU�c���p�X���=9yلPzW���IZ��������|�kI����fx@�S��?��(���kX3��H��D�5�&�xt�C�Z%�O�-ۡ�M��N�G&F�abS�o��\Ï&~R����Ń��n��JI����]�\e��@$e8�1E;��>9�U�Lr��o��üV{S��y�E�U�-(�B�T0�G��T��l�����v�ͨ�0y���\U5m^.V�D5�����ׅ,y-�JEz4;���e}����$��d�}]�Aor?e�c�
4ڤ[�=.
@ܫ��YK��"x����fS���a
�[w&D��N��K/%���e� M�c}����(�s�X�e�8K3t E��>$>K��c�Q[G<5lD�!#z%����#Z?���������6�r��]��� ����o��H����o	�̡f�4M�t�X�_��@��9��Ʉ8����&\:3Hܫx��'ެҿI���ǔ�K�*��ǉ;J3f�~���"3��CgN�x�>�τ!\�g%�W��IZS`��/PK
   �N�@��=��  2  4   com/lib/udacity/simulator/view/SimulationFrame.class�TmOA~��^{R+(��k�ߋ��byQ"�o,���ޑ�-H��)�&� �q���K������3�3����_�(ൎ�05duĐKayc��a\G"�X&t�"eRCA�S'e*�;j��Ľ$�+�:⑚��˴�k����!����B��ޔ��"Co��B�=��݆�F�0��Щ7\.	��=�2LT�~�r�-�a�#�6��=G�[kz)z��d�-}�a�����(t�@ӎ����y��̋�u�xɷ��xJ;vV��i`W5<30��X'E�����`�a`��q��Kk�lT��ߐ��Q���y�`�^��M�!�,��a��KT,�i+V���.2*��V��x5k�m�2UgG�����m�M�tn����'E�����qc"��xM-d��;�1%���{ԭbds9����#��呬	��\r1�'d��O��C:�:�S��'Âpj�2�e�oxvȠ�ezT�d��xÕ%��ʮ�݋�� ���q��.��z��-���Z�>ꯧA��i����!w����F�]���s�o��l	e��$9�d�=$G�m�LNA3}M���̜mK=����v��7q���t�f$�W7�8�K4q�St�PK
   �N�@9�¹�  �
  4   com/lib/udacity/simulator/view/SimulationPanel.class�U�SW�ݰ��@�,)ű!�iѦ��B-(�m�Kr+K��.����Щ�O���c;��S?���_�V�9�
A��̞{�=��;�{����Ѓ;a��Tp:L��gU��9�EЏ&o�8Ax{0�!\�N�a2��b��.�cn���L�0���dW1��Z�x/���{���0TLDi��5!m��f���!�ھl�q��;aXҏ�O�s~�2\284���',s:��6R���(j�vb�lwB���S�Af�jr�y�8ifL��@g���uN(}ٴ��3�
4ņo�F�Xr�m#7k�Ϯv�5Rs#F�1mI*����6�]p�%[:�L��-e�M��~��B�~LZ� �v�R���+mY�,35�b��͛�Lk��p�h�3^�k{�A��W1���M��a��yP��U/�1����r�-%�8}S�\Y�4|[���ł�EK�kXf�	򔈆OY��S�g�ř�br����Bŗ��-��2�1:���X���Z�m��[�q�߃�s�:�ES.m�{��H�<�p���Lb��ٲSk�MǕi� -����Fpt������qG�F:�T�����d����P��Y�����.�:k8�2_@t�&:�	�%{���(4���Hި��a�{�=t��V��H�nlʩ
$��'�ȥ�m����r�$��!m�0���2ϑ��9z?B�uA�3��$~�L��T>b��)*גaYt�:v�Q0"$��4��lj�C�����7w'6H?nAݓ:M�&�Ƕ7����a�iå����{��N/t^B �Hz��z|}8H�"O�[�ŵ���V�|�q�h����>�	�Z�/�@ͽ��Q����[&޵	���#�5�6��U�4x�P�Ҭ������(�EH�|���!Z�C4�8��؟����H�	5�a��w��;Uf�O��hR�wm��u4�^�]D�5įD]YA(�+�%�=�h��ƢU�*�,�� oe��X�Йkd��7��!�4�z��Ul H�����
ֺ��P�~�������N��J:�g�ɀ�VZH��ʀ��+��^��JQ��у�4��\�5������y�te�մ��y�mb�}��ar����'��h���o�@��EW+��jU�v�Pq��k}��^u �GP���LP��FTD�'���q2�-�[�w?Ƚ4�'ʪ���P{����ޝ��"��wI�J����d�t�PK
   �N�@��.�  ]     com/lib/util/Random.classU�=N�@��9q	t��d��D�$
���g�%��6����CD4 Qp �=h��Bb�7��Oof?���b�Fm5�X�X��S�R"�*U��:�����fBg��si~z_��ӈ�)��#B�BB}��%���.;y�*����/2�鯺��g��R�b��Fˁ�]B'J��X͆y�����dɝ�ŭ�oq�=.^��a��j��@�}*��t�i��9x=�<=�۬����`m^`xE��#�*"`�V����#^�.�~��h�ȓC7�PK
   pn�@mD�w�  �  '   com/udacity/simulator/BicycleModel.javauR���0� ���������!�u8�pkс��XW�6,��ܿ���(98��G��=�b��/	TuʬɳV�2�gΜZ�\5ϫ�jY��5
�E��Q���Ri��Z^V��v{.��h���:TO��Vy)SIB	uυG窵�[Ǡs`��CS���;��[���u8�[!��G���%!���p��<Z��D�5���h�����E*~��o1\0����(}A.29I�d*sZ�i�HK�A}��y�s/�S�����5 "sH��.�S���]��}Kc�%�h�&���^9��Η���];ΔI�/�-�g����掩�3��Xn��6�,+��Ӽ�V��ϔ\��$߳u�x��޲>"$���p�U�Kx�5|�����b�y?�'���mJ(�<��EV]�<�?��	O��PK
   5n�@b~  �  %   com/udacity/simulator/DefaultCar.java�Xmo�6�� ���m���N�|�R,K�,X���5���h��L
$����w|�H�r� 
U"�;ޑ�]�����E�����pJ�*�tQ�Xq1���ݡ������8�O*9幙i��\<�T�X�����2"(��N��-ʓ�h�V+͓k�"%���2����W�@�Ҕ3%x����dA���&sIٷW����k�L�T�J&�X�Yᴶ�FU�ft^
|Ʋ����,�����i��K�ޓ.s���HI�C���<���
A�"���XTI����` O4@��83T�R�͸@V��B�P�����-'М��S�B�8/�D3�H=�\a��ӣ., ~1���yC[/Ҹ��H�s6GX�'�2�~RhN��[o`�f��Z��fF
AR�K67XJEO�94֌����h�	��E	_9OqN����{�Z��*r��%�<���e�fV�(��9�R�b-a�^���[���c��|[�E� �ܶ#��.���Y=0ic?r�!YA[e�]��Y$�$�X�sb�H.!�0��ٯ��tF$$3����/��nq]�����5bm^L6����u�����s�c�z^W/�Q4�	����Z�ŝ�Q}��a��� ���B��wK���L��5�kn��!ŝb�:"�b��S�vH�z~MB���12G�v��.	�ñ<Fc��ht�^ Y�f��e`$B�ZTҿ��ЭҒ��\_�#r
�e��݆���z�3����L�&����ucᩭ�k�H�C�?[z\�_EB]3�r�|Q���
��k�B��4�92BqE�>k����fRs�*� �)B�U�a��=լ�	���K���?����^R�y?F� X�q���v\s�@!�"mTwZQ��O�h�+M�B3,z�jF�5�����v�/P Ӈ�l���	�$�	���Z��ջ]��Y$D+�����<ӥ����)σʝ�I�l�D)"~�5����D�ŗ��)Jm�;/��pT��`�.A[[jAs@S�a�
�2k�Z�B�Qt��=XiD�R��OE����x�M5,͜������	��1���}k�ޅ$ںMYQ�Ȣ�"ad��q)%�,
��0��Ac�nS�lܶ�ӂà�!���mc7�9�V��o��C�A=�bdv�.���A�XŨ�T�\�A�{-��Z�d�Xn#��n�.��"4�5��?��hn���7�������ܽ�£��ƺ��,�o���m��D�1z�+�x|{�g��܀���R�R;�D��eB�������5WZs���)�k�5�10��mm�S�s�ݖ6ha��NT�&q}�Z/��r���.T���j��sNk�������eqx�r�ŀf�EP��_"���Ul�ѱ��J
,$1�Q�K�S_E}�A�-����UYk7��A�7��(���^oKk�~��@���h��Z�Zo���)�{]P��VhB9~��- m/-_����v�m@wm ���ې-�ז�k�VhD��Vs�S�%G5bM�ۺg���;��k��[l�8I@�S����Z���A4�"���_�"_��5�w�+��ݰ�x0獿NM�]ch]#��)�ל��-��k��1�')���u�Z|>O�n�r."�L~��tN�����ӏ�h9D�L��٨�[m����ד�Ӌ�ˋ�ۋ��C��|���׫�!|&�/D�b�"Ѓ��x����j�h��Ч���lcʨ�<�/M�U]x{����s{�n�����IZ<�^����l{3�-tI�j`
��PK
   /n�@y%��  �  &   com/udacity/simulator/SensorArray.java�V�n�6}V��a�U{{_o[d� @�5ji`���h�[�H*���wx�Ų'/	EΜ��93tN��HJQ,�Q��Q����2Rl[dD9����b�\H����W�K�?�X}�:=>,4ˢߥ$�L�ù9��Q�F>>"k�%���~�a�������i�{�͍�&<[{��Xg,FqF�Bʕ�6~�R�a��z}���
nn�KąF�fbM2�4X�HX�_�&��h�\@d�	����Ң�7� ��rW�K0E������*&[*���<cǸ��'O�w��sΩ�h ���y7Fg��&R���ql�x�m�LL�	�8}�ušq�3SQ	&Fp������J��Dy,APɤ(n�(Q��G �
��HE��QJ�w/���e��ƃ�ݴ��Kx]�A���=pMS*|�#9��h0����8u�=P]�\�r�vꃫT�4��sr� }.W������a&���jYE�Vz�=
�%�����{��RdZ��ݫ�[�َf86;��pdO�'�6XF���C�O�ͧ��������&K�g��f�I���b��Iu!����~�_���.��_�V��z��z.��/(ߗ}���/���'9�v��+�Y.��������\>�1��u�:;Ù�
eF�q78aϞGe�<�W��+����.by!�S-�A1�z�
&�#�@D��n��2t�����$�����=��~Z�H�����X�~@W���WGUgv�ÿ[�2���Ua�[��r�kk9`�ƴ}>�OV�v]y�J�Nk_D'���b.3��@#���
��C�|��P��ti�u>r/�v:��jL��>ݍ��p�|NL?4?�P��/�۾�3ݪQ\��o{v@�4Q�[��a5���'i6[��c̌��1 g��9�%0<ր�n?T�GwwG}_��������ݩل���?�PK
   #��@�J�w�  �  %   com/udacity/simulator/Simulation.java�V[o�6~v����>IE��}��bú���3t��Z�c�4)������M�eyM$�y�s�΅lI��<R���l^u���V��:N�T���3�j�2���I�d��q��4�e'�_�j�&�t�����c���)��0^����#�&����f\:~�Qɖ*è�3:�vE��(R]�B�0�� ł=v��9�>͙?CRlT�������_hm���ft�)~$�rGQ��9���DkH @����0>uB�,/�?�8������l�*�&��	�#t��g�x�w�!�RrJ�N�,�4S<q�Ø0`؊���l�Λ�\z�T؟PwJa>���<J��Z�����ɀDX3����P�����yh�(�Ԓ8	@�C��A8�Y�֚57�Q���Y)$@���@&)̒i��.HǍ��-��O�`ޗ��l�gu���H����c�t|�M��(+�M�#��ߤ>���*F�o��E�S�tJ���Ga������A.�9��T�1�����!���ȭE&�e�;z�k�cf����o����c�ӏj��I���c���$t?I�Cvc�����,w���s�z+ꥒ��K�ޖ�-L<q�1
�
�'U#���G���=G�&�Nn[���v���K+w��avbX�e�0�Eq�x�G���<b2����_�y=DU��ź��-O7�_�#��4�+fF!���,� �� �ҥ�L�.�!�t�l+뮰��d(�CXHU@~�B?ĭ	�'��l�e��Owk�k� Ol���@jQ_�`�S��g�pA������`&��Ѵ?����Ka������������6Kd�Om�_dm���p�����϶ê����3��
1P)�l�������"�<��;a ���������*E[��CK�k�$�d֨-+����"��4ŗ�I1Xx�!�I6Ni����椹�{f|d��M���V��Hu��i^��1VZ�A�����=>�S��>o��RyV� *��0��M��%�K�d�ǄXz��zec�um��֟��M���Ń���<2�n�%+����G�/�1�Fw��+q��L@j{�s�������TC�ù��Z*{��&|zy��/0��O�����f�<h���=��?-�'���DM�8��'(��D�9��\�.a4F�w�{��fb/)٢e[�����3��PK
   쌡@��|  �  "   com/udacity/simulator/WallMap.java�TQk�0~v ��֗JD���]ٺ���%{��q�e�E2��4���I��4�#`d���>�}�]�\b�@ڕ�4u���FxZ��u���p@�ʺ ����ju�9��9�$��MOr�d@Sju�#+��E��ʧ
su,���J�^FH�2K�?���&>T�\���{��Z��
����A֥�Ӯ�����Gn��t<�c(1�c0j�Bި0�^T�-�-�ήRs,Ppg���HU�f�͡o@���0�Rho+8���~G�MF%j�u�d�Eڝ��p��P��w�J}�t
O3@W��G�JS`g��f�,�k
r���b&��$���tB��sw~լZ�9k:�9��MP�r�B�U\���g|���qy��$���l]Y��t�۳̢_R[��Nxn�Vh����to� /#H���ֱ]��ઽvo���9!�	HƳ(�9�3jg �ZU�M����5��j`���]i��*4 ֌�f2���n:yl�9]z)
�����V�PK
   ;I�@}.$S�        com/udacity/simulator/World.java�V�j�H��@��İ g��,��ݦ����mHa�2���c��b����3]��)X�4����2}�	�H���!)bq]���
A�T��|�I��}���5y'����?(�-y��!���	"_��X,�b�y�qqI�s�?-4�ZɌ)�Y���ـs�h�sr��'Ji|�Sr�d��I�h���%�����S��E�	i�Mc���dE(x��y�R�PB�KumO���>�&�Ã�������~YB*5�A"dH�E"�V�������L��c�jX�X/�{�KƓ����gs�Xw���6C�Ҥ'�)����8T������#��<�5P0���}T��0��'yu��t�O���:=*������0��4�����{�g���m)�����4�13�Fv3�*��#T�.�aE�rd���OL)$5�$�AH7�4�������1��T��)�Q�3|	2��x�2�M
<�p<|=y�M|��E���m2���/U�Ҁ~m4��/��/MPGS���o>U}�)��@/�\ۂ��%T�UIa��r�̴_0t6O��/e�}2���M�BXB�T��.�%i���8�9��5�V��٬�je�\��LI����	�1�������W��)��J�=0��/@��X0��:���ӹ����A�Q����5[�=�=�j�8]*%��<�iE됇d��F\��m�
[����kz��ig�ݱO��K$w�]_~�����͇g��c`��%�b�EE�>.�
lsn�sr��7S�ٰ9�֥�B(!9�v������W�EBbE��v��M�;�=Cm�tKxS�(����&�6�`9�VY1�,��ky������3�N��'쬗\�J9{�1QԚ�<Zp!npU��3�S��Y���*��񶢵q}�yv`���pOڳ�^���}o������"~���r:nU��:88��|V�QB��m���<�5z[�����L��ٍͧ$��pp���}cѝ�gR5}2�(�P�c��7lme>�ww4�Xs�Ř�`��IC��$�>�����w4ԩ4�g�O[_ED�4�]���$�,!��ҿ�|G`6�W2.�~�����Y4�7J/ɭ��a���{(0���H�92
6�������}��#|���GX�"AK"D<�r^U��PK
   ln�@����z   �   /   com/udacity/simulator/abstracts/Background.javae�A
�0E�r�YV�\�+�^a:M��S�	��w7ե��?��W�'��sB���Px���9�P,#Y��n��0/���Rֺ���˻SC���U4_��[�nE������?�;f3����PK
   dn�@Y�2��     (   com/udacity/simulator/abstracts/Car.javau�M
�0��r�,u�t%=��nt9�NKt�������u���=x3�	Fr�'�1��F���ʠY<�����ƚ���bR��\�謔���(�GB��j��38���t��4�a�ަ�iuJ$�L�����6'��L�T���ݬ�PK
   `n�@�7*��   R  2   com/udacity/simulator/abstracts/CarController.javau��j�@D�]��cl�CϹr����.ݍ�V%��n�RB0�y3Rx��$7)���Q�viJ�S"m�-����n����X{
��AN��+�������OB���82w�j�@z����<���7j����Q���E���M��
&خ7�Ϭ��Ŷ��?K�P��V�C�����H��D��f����_��PK
   Xn�@��o�   �   1   com/udacity/simulator/abstracts/Configurable.javaE��
1Ek��)���Zj��?0y��ٝ0�,���

��p*��	O��w=b }�FS/�,}S���`�54U�;.�Rq�D)��0\ϧ�2�$a�2�ЬI2�dM��PX8�i삾$��e���Y�"Ƹ��+B�}�ok>PK
   Tn�@�����   n  7   com/udacity/simulator/abstracts/SimulationListener.javam��j1D����@P��].�&��pe\�I�eI+V{!��#��@�na���t�8p�l��.駭����bq�*�n:�J�E��h�C�V�������,S$�5�	]��C�_�j�A:�ՙ�_���M�(g�18�� O��,�d������s���SdT�Blw�U>�p]!LA�o��Q�W�6���k��0���(�zy�ݙPK
   Pn�@ V��   �   5   com/udacity/simulator/abstracts/SimulationObject.javae�9�0Ek,�S��mJ�(A��%a�c[�8�w',���-�9a���QyҪZ4�WUh�9f��pFå�B
S�N���j�1ɔ��S՞P`�;4��a�g܅]��1t�׌�;)nR,>�)����e���d�]�����x{����)蟦�PK
   ���@�M���  �  -   com/udacity/simulator/view/ControlPanel1.java�UMo�@=��0�i��z�����J�(���؃�fY[�kӨ��~`ch��R��7��̎�<�!��T�-S�p�H5_���\ъ�f���{|]���V1�6�^�*Eu��Ҍ���Bi�ebx.�����%��;L���}?��p��OW�1��2��Hl&x���u��M���Ltm��z���3>�����������\�@"��0ɥQ��G�?��TC�Xf�k+WC�����~�W��W� hc�%��	��@��LܣҖ���k���͸ud�tWn�vF�S�}|��b�.|v�v�؂��Ȭ����V�v�$��ٗ7�rr�J�'񸍡,M��"�:>"/��	��Жr4p$��6$5B��g�D�fXsh��".E�8��0��Ԓ�^��{H�r6�~�O�<�����B���]ݫ���|5nQ-s�Ɣ��70�c�{��Ľ��Y^�IM�c�,n�)��])��V�`�X��تԠ%��V�,`n'����=��)�A{��F���m���v�BK�<s{�|���"��.��
+f'��<�h�è�qiĵ��4��8^�@��2�87�)�0!>��R'v�!�-����}GjV ��g+ww��Y|����Ԭ����X��f�]vv�>�����gޙk�;j^�`�3�Y���!l��O���E���z�6�տvr��:�{z��q��2%��oX/�v���9_�5
�HF�������U�z���oPK
   �N�@�e�=1  m  -   com/udacity/simulator/view/ControlPanel2.java�T�n�0}����Q;��T�!�elꄶ���y4�%����v�h�ώI�P�!�ܓs�uX��e�ʩ�KZ�,ᶤ��`Vi����>��J[��6����7J��g�T���q�����r%���?�7%�#�{L,���C;j�\f��Ma������(N`��/Ez'���X���+,t���>��(j:s����+^E���R������V+Q�� �6��@NY`���9���{k�7�"��Xq�%30�9�P7���3���l�i,��{��ۇ��_��_���{��!t'.i��ɇ��Gnhc�Y7^Ë��^�=���!�M���ѨE�,M��/����j/���ˠR�Ԡ�^]] ~{.n�.�sM:��#^��Ƒ((T4g�샜wXtz=_+����@���s�2'���}%�\��c�Z���mO�Umޡ^)�cJZ��tvA�G�"����U�$���q��"���۹&o��5]3m��y�p�ᾖ�^��Ǉt�y�֞S�P�۝���z!����xod��k,&e��CU��PK
   댫@�<⇀  �  /   com/udacity/simulator/view/SimulationFrame.javau��k�0ǟ-��ǖI�>d/S�6Ď�~�IlϚ-mJ�ڍ��}YZ�)
i��>��~˕4��B"r�ٖT)M��&���ZHr`XO|��X^
��(��&�B�(�[T�|U�"#�w����^n�jNL�/�-g	$�*��-���H4�}����d��6`;VP\(���W��xy����ɠ�����A��NE����~lu�KX�`�58h���Th�o�����/:P���D�no\����출c�X�~���팺��r�	Bh8��}YC�$��r=>ю��������h.��_�l+�VTf���h4�)��~��Ah�,�� �����e{���z��w�3�ъ�)
���4cJ���M��L�jn����YPK
   Gy�@-&|�'  �  /   com/udacity/simulator/view/SimulationPanel.java�V�n�0=ˀ��G����X7E�&�	t;R�XfBKI/B�/[���	�-`��p�ͼѣ+BH���Y���L�X�ŒU
�b���G�[T�P螬&k�?
R���a��y���"EΡ�+(�*�.�TP�8ua~��m�\�"�_nH<��y�~���>!��R	B��]���3[�Z��QD9���F��I��!]��Bw!�^��ѯ�(�[H*���+G�,r$A0¿��:������\N�#�.�asQ�
��ʹm�;���ֻd��V�qX?�a��H͙��m�'�H��u��ĸ]���+�e��J���h0�n�P��])��@`��m*�'::b��#�L�.�B�K���l�7姙�{K��dѬq�~T�7��m�(*��r�9(L �A5�'��n��fh7��,�o�f↫4���
�9��u)xf�:��]%sb,����O�D�Y���ߍ��"�MTmt$׏]�Y��oѱ���\�u��w�Lc�U�K�3H\���n�Z'v݆A��S��\�{M4��f���~��ny�^O�-p Y�+<k��c����.s��m�C���-��$��]&i�I�.0K;̺�.m������>��lk[SmM�V��^ίH���Dk`\�5d�ӽj�6��GSsb*�������d�8�LꅠЧ@�0&�J�e�D�I��0��1�B��,�g��v�=���J�E�@(�]ܡ���� M�[�'L�.ue��J�>M
%��HAz�rԫF���h����;����{rl�/������ӟ�PK
   wn�@���   s     com/util/Random.java��Kk�0���?����(�R�o�R���7��n*��V}��^%.�r�eYvg��;n,�W���ɭr��a\;2`��3r�{��r+�������w��!�����#F���B�j����{h�z^�Z/�����^�#8�%�'�����l�OG�<�(B�E�<F�KH�?6���Q	�I����a�?�
�E�8��4��J��Я��/��>W?PK
    �N�@            	         �A    META-INF/��  PK
   �N�@W���^   j              ��+   META-INF/MANIFEST.MFPK
    ��@                      �A�   com/PK
     n�@                      �A�   com/controller/PK
    ��@                      �A
  com/lib/PK
    ��@                      �A0  com/lib/controller/PK
    ��@                      �Aa  com/lib/udacity/PK
     ��@                      �A�  com/lib/udacity/simulator/PK
    ��@            $          �A�  com/lib/udacity/simulator/abstracts/PK
    ���@                      �A	  com/lib/udacity/simulator/view/PK
    ��@                      �AF  com/lib/util/PK
    �o@                      �Aq  com/udacity/PK
    �M�@                      �A�  com/udacity/simulator/PK
    ln�@                       �A�  com/udacity/simulator/abstracts/PK
    �N�@                      �A  com/udacity/simulator/view/PK
    wn�@            	          �AF  com/util/PK
    �N�@                      �Am  lib/PK
   �m�@Ȍ���   �             ���  com/controller/D.javaPK
   �m�@��c  �             ���  com/controller/Element.javaPK
   �m�@.)�L�      !           ���  com/controller/ElementHelper.javaPK
   �m�@�<�P�   E             ���  com/controller/I.javaPK
   �m�@6|eq�   �              ���  com/controller/Link.javaPK
    n�@װ.��   @             ���  com/controller/P.javaPK
   �m�@p�&C  a             ���	  com/controller/PT1.javaPK
   �m�@	�:y+  �             ��U  com/controller/PT2.javaPK
   �N�@qt��3  �             ���  com/lib/controller/D.classPK
   �N�@]���   �               ��   com/lib/controller/Element.classPK
   �N�@)�=o�   �  &           ���  com/lib/controller/ElementHelper.classPK
   �N�@Fb�#  �             ��$  com/lib/controller/I.classPK
   �N�@�D�  �             ��x  com/lib/controller/Link.classPK
   �N�@�g8  �             ���  com/lib/controller/P.classPK
   �N�@\�3��  �             ��  com/lib/controller/PT1.classPK
   �N�@ʀ��l  �             ���  com/lib/controller/PT2.classPK
   �N�@��dX�  �  ,           ��v  com/lib/udacity/simulator/BicycleModel.classPK
   �N�@(o�L�   �   ,           ��Z  com/lib/udacity/simulator/DefaultCar$1.classPK
   �N�@��wIN  -  ?           ��7  com/lib/udacity/simulator/DefaultCar$DefaultCarController.classPK
   �N�@}UA>�	  �  *           ���  com/lib/udacity/simulator/DefaultCar.classPK
   �N�@�E  �  +           ��'  com/lib/udacity/simulator/SensorArray.classPK
   �N�@�sa��  �  *           ��V-  com/lib/udacity/simulator/Simulation.classPK
   �N�@�>�ķ  @  '           ��a4  com/lib/udacity/simulator/WallMap.classPK
   �N�@��R��  �  %           ��]8  com/lib/udacity/simulator/World.classPK
   �N�@]���   �   4           ���?  com/lib/udacity/simulator/abstracts/Background.classPK
   �N�@E�   D  -           ��q@  com/lib/udacity/simulator/abstracts/Car.classPK
   �N�@�62ؘ   �   7           ��wA  com/lib/udacity/simulator/abstracts/CarController.classPK
   �N�@��*�   �   6           ��dB  com/lib/udacity/simulator/abstracts/Configurable.classPK
   �N�@�Ό �   q  <           ��?C  com/lib/udacity/simulator/abstracts/SimulationListener.classPK
   �N�@>~Qj�   �   :           ���D  com/lib/udacity/simulator/abstracts/SimulationObject.classPK
   a��@�K���  �  1           ���E  com/lib/udacity/simulator/view/ControlPanel.classPK
   �N�@�hNK�  �  2           ���I  com/lib/udacity/simulator/view/ControlPanel1.classPK
   �N�@8�1�  �  2           ��nM  com/lib/udacity/simulator/view/ControlPanel2.classPK
   �N�@��=��  2  4           ��jQ  com/lib/udacity/simulator/view/SimulationFrame.classPK
   �N�@9�¹�  �
  4           ��CT  com/lib/udacity/simulator/view/SimulationPanel.classPK
   �N�@��.�  ]             ��qY  com/lib/util/Random.classPK
   pn�@mD�w�  �  '           ���Z  com/udacity/simulator/BicycleModel.javaPK
   5n�@b~  �  %           ���\  com/udacity/simulator/DefaultCar.javaPK
   /n�@y%��  �  &           ���c  com/udacity/simulator/SensorArray.javaPK
   #��@�J�w�  �  %           ���g  com/udacity/simulator/Simulation.javaPK
   쌡@��|  �  "           ���l  com/udacity/simulator/WallMap.javaPK
   ;I�@}.$S�                ��o  com/udacity/simulator/World.javaPK
   ln�@����z   �   /           ���s  com/udacity/simulator/abstracts/Background.javaPK
   dn�@Y�2��     (           ���t  com/udacity/simulator/abstracts/Car.javaPK
   `n�@�7*��   R  2           ���u  com/udacity/simulator/abstracts/CarController.javaPK
   Xn�@��o�   �   1           ���v  com/udacity/simulator/abstracts/Configurable.javaPK
   Tn�@�����   n  7           ���w  com/udacity/simulator/abstracts/SimulationListener.javaPK
   Pn�@ V��   �   5           ���x  com/udacity/simulator/abstracts/SimulationObject.javaPK
   ���@�M���  �  -           ���y  com/udacity/simulator/view/ControlPanel1.javaPK
   �N�@�e�=1  m  -           ���|  com/udacity/simulator/view/ControlPanel2.javaPK
   댫@�<⇀  �  /           ��\  com/udacity/simulator/view/SimulationFrame.javaPK
   Gy�@-&|�'  �  /           ��)�  com/udacity/simulator/view/SimulationPanel.javaPK
   wn�@���   s             ����  com/util/Random.javaPK    F F �  ��                                                                          testMap1                                                                                            0000600 0000000 0000000 00000000072 11746200262 011164  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   r,0,0,10,600
r,790,0,10,600
r,0,0,800,10
r,0,590,800,10                                                                                                                                                                                                                                                                                                                                                                                                                                                                      testMap2                                                                                            0000600 0000000 0000000 00000000246 11757610342 011176  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   r,0,0,10,600
r,790,0,10,600
r,0,0,800,10
r,0,590,800,10
r,100,0,10,300
r,100,450,10,150
r,200,450,10,150
r,300,450,350,10
r,350,200,10,250
r,650,450,10,150
                                                                                                                                                                                                                                                                                                                                                          testMap3                                                                                            0000600 0000000 0000000 00000000253 11747721100 011167  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   r,0,0,10,600
r,790,0,10,600
r,0,0,800,10
r,0,590,800,10
r,100,0,10,300
r,100,450,10,150
r,200,450,10,150
r,300,450,350,10
r,350,200,10,250
r,650,450,10,150
r,290,200,60,10                                                                                                                                                                                                                                                                                                                                                     testMap4                                                                                            0000600 0000000 0000000 00000000337 11757575730 011214  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   r,0,0,10,600
r,790,0,10,600
r,0,0,800,10
r,0,590,800,10
r,100,0,10,300
r,100,450,10,150
r,200,450,10,150
r,300,450,350,10
r,350,200,10,250
r,650,450,10,150
r,290,200,60,10
r,450,130,140,10
r,580,130,10,170
r,360,300,230,10
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 