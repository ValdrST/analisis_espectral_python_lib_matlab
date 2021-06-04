function [xn,Ak] = analisis_espectral(x_file)
  %*******************************************************************
  %           Lectura de una x[n] = xc(nT) en archivo.txt
  %*******************************************************************
  fid1=fopen(x_file,'r');
  xn = fscanf(fid1,'%f');
  fclose(fid1);

  Fs = 32000; %se debe sacar de antemano
  %*******************************************************************
  %           Análisis espectra de x[n] mediante la DFT (via la FFT)
  %*******************************************************************
  N = 2^12;
  t1=2;
  n1=round(t1*Fs);
  n2=n1+N-1;

  win = blackman(N);
  cg = sum(win)/N;
  xwin = xn(n1+1:n2+1).*win;
  Xwin = f_fft(xwin);
  
  Ak = (2/N)*abs(Xwin);
  Ak = (1/cg)*Ak;
