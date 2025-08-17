[y, Fs] = audioread('morse.wav');
y = y(:,1);              
y = y / max(abs(y));     
env = abs(y);
env = movmean(env, round(Fs*0.01));  
th = 0.2; 
binary = env > th;
diffs = diff([0; binary; 0]);
onsets = find(diffs==1);
offsets = find(diffs==-1);
symbols = {};
for i = 1:length(onsets)
    dur = (offsets(i) - onsets(i)) / Fs; 
    if binary(onsets(i)) 
        if dur < 0.2
            symbols{end+1} = '.';  
        else
            symbols{end+1} = '-';  
        end
    else % silence
        if dur > 0.6 && dur < 1.2
            symbols{end+1} = ' ';   
        elseif dur >= 1.2
            symbols{end+1} = '   '; 
        end
    end
end
morse_seq = strjoin(symbols,'');
disp("Extracted Morse: " + morse_seq);
fid = fopen('morse.txt','w');
fprintf(fid,'%s',morse_seq);
fclose(fid);
