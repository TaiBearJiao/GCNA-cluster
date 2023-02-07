%Setting thresholds
threshold =[0.293775,0.211336,0.18187,0.161109,0.143606,0.124354,0.051176];

matCell = cell(1 , 178);
for i = 1 : 178
    name = sprintf('%s%d%s','mean_mRNA ',i,' .txt'); 
    mat = importdata(name);
    mat = cat(1,mat.data); 
    matCell{1,i} = mat;
end 
for i = 1 :7
    scoreMat = zeros(178);
    for p = 1 : 178
        mat1 = matCell{1,p} ; 
        for q = (p+1) : 178
            if p < q   
                mat2 = matCell{1,q}; 
                mat3 = mat1-mat2;
                mat3(abs(mat3) > threshold(1,i)) = 1;
                mat3(abs(mat3) < threshold(1,i)) = 0;
                mat4 = ones(size(mat3)) - mat3; 
                %Labeling equivalence matrix
                [L,num] = bwlabel(mat4,8); 
                S = regionprops(L, 'Area'); 
                areas=[S.Area];
                [m,ind]=max(areas);
                scoreMat(p,q) = m;
            end
        end
    end  
    scoreMat = scoreMat + scoreMat';
    filename1 = ['Score' num2str(i) '_8domianMAX.txt'];
    dlmwrite(filename1, scoreMat, 'delimiter','\t'); 
end