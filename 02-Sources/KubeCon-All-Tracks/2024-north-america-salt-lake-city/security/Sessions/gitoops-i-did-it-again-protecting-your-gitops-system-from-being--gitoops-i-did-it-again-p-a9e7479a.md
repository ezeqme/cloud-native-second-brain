---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["AI ML", "Security", "GitOps Delivery", "SRE Reliability"]
speakers: ["Oreen Livni", "Elad Pticha", "Cycode"]
sched_url: https://kccncna2024.sched.com/event/1i7nd/gitoops-i-did-it-again-protecting-your-gitops-system-from-being-used-for-privilege-escalation-oreen-livni-elad-pticha-cycode
youtube_search_url: https://www.youtube.com/results?search_query=GitOops...+I+Did+It+Again%21+Protecting+Your+GitOps+System+from+Being+Used+for+Privilege+Escalation+CNCF+KubeCon+2024
slides: []
status: parsed
---

# GitOops... I Did It Again! Protecting Your GitOps System from Being Used for Privilege Escalation - Oreen Livni & Elad Pticha, Cycode

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Oreen Livni, Elad Pticha, Cycode
- Schedule: https://kccncna2024.sched.com/event/1i7nd/gitoops-i-did-it-again-protecting-your-gitops-system-from-being-used-for-privilege-escalation-oreen-livni-elad-pticha-cycode
- Busca YouTube: https://www.youtube.com/results?search_query=GitOops...+I+Did+It+Again%21+Protecting+Your+GitOps+System+from+Being+Used+for+Privilege+Escalation+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre GitOops... I Did It Again! Protecting Your GitOps System from Being Used for Privilege Escalation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nd/gitoops-i-did-it-again-protecting-your-gitops-system-from-being-used-for-privilege-escalation-oreen-livni-elad-pticha-cycode
- YouTube search: https://www.youtube.com/results?search_query=GitOops...+I+Did+It+Again%21+Protecting+Your+GitOps+System+from+Being+Used+for+Privilege+Escalation+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Pz_Oua4L_AE
- YouTube title: GitOops... I Did It Again! Protecting Your GitOps System from Being Used for... O. Livni, E. Pticha
- Match score: 0.959
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/gitoops-i-did-it-again-protecting-your-gitops-system-from-being-used-f/Pz_Oua4L_AE.txt
- Transcript chars: 21739
- Keywords: cluster, attacker, argo, security, application, instance, gitops, repository, manifest, server, deployment, research, changes, access, within, environment, malicious, network

### Resumo baseado na transcript

good morning everybody and thank you for joining our talk gups I did it again protecting your GTO system from being used for privilege escalation thank you for being here today gitops is a rising star in the devop and clown native community and from our experience it seems like almost every organization is adopting it these days in this talk we invite you on a journey to explore gitops from a security focused perspective we will delve into the mind of an attacker examining kp's best practices and architecture

### Excerpt da transcript

good morning everybody and thank you for joining our talk gups I did it again protecting your GTO system from being used for privilege escalation thank you for being here today gitops is a rising star in the devop and clown native community and from our experience it seems like almost every organization is adopting it these days in this talk we invite you on a journey to explore gitops from a security focused perspective we will delve into the mind of an attacker examining kp's best practices and architecture through their eyes Our intention is to equip you with a deeper understanding of gitops and practical tools for its security strengthening your entire organization security now just to get a general idea of our audience today please raise your hand if you or your organization are active users of GTO okay okay um now please raise your hand if you're here to learn about gp's hacking shananigans okay so the same people perfect I promise we'll have something for each group so let's begin in our talk today we'll have five key steps first we will explain why we identify gitops and Aro CD as emerging Technologies worth researching then we will study gitops how how does it operate what is the gitops manifesto and how does it look like from an attacker's perspective then we will share in the exploit part we will share our research story detailing how we discovered a critical vulnerability in ouro CD system and its implications as well as sharing insights on how to conduct a similar research after that for the GTO security versus reality part we will examine gtop security best practices and identify scenarios where open- Source projects and Cloud providers require a bit of extra effort on our part to to avoid being vulnerable to GTH Up's attacks and finally we'll wrap everything up by discussing our practical next steps and we will share a surprise to to help you apply what we've learned in this talk sounds good perfect a word about us my name is Orin I'm a security researcher at scyon I have seven years of experience and I use to research care bus and networking and currently I research um supply chain and Cloud security hey my name is alad I'm security researcher at cyod I also have seven years of cyber security experience I'm mainly focusing on application security and supply chain security perfect so let's begin by identifying a trend but before that I I want to share with you the story of how the idea for this st came to life but it's not for publication so
