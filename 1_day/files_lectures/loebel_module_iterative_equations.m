x_fit(1)=1;
for n=1:8
    x_fit(n+1)=x_fit(n)*(1-U_fit)*exp(-50/taurec_fit)+1-exp(-50/taurec_fit);
end
x_fit(9)=x_fit(8)*(1-U_fit)*exp(-550/taurec_fit)+1-exp(-550/taurec_fit);
alpha_fit=A_fit.*U_fit.*x_fit;

V0_fit(1)=0;
for k=1:8
    v_max_fit(k)=alpha_fit(k)*(alpha_fit(k)*tau/(alpha_fit(k)*tauin-V0_fit(k)*(tauin-tau)))^(tau/(tauin-tau));
    V0_fit(k+1)=V0_fit(k).*exp(-50./tau)+alpha_fit(k)*(tauin./(tauin-tau)).*(exp(-50./tauin)-exp(-50./tau));
end
v_max_fit(8)=alpha_fit(8)*(alpha_fit(8)*tau/(alpha_fit(8)*tauin-V0_fit(8)*(tauin-tau)))^(tau/(tauin-tau));
V0_fit(9)=V0_fit(8).*exp(-550./tau)+alpha_fit(8)*(tauin./(tauin-tau)).*(exp(-550./tauin)-exp(-550./tau));
v_max_fit(9)=alpha_fit(9)*(alpha_fit(9)*tau/(alpha_fit(9)*tauin-V0_fit(9)*(tauin-tau)))^(tau/(tauin-tau));
v_difference_fit=v_max_fit-V0_fit;