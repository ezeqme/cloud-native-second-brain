---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Cailyn Edwards", "Daniel Murphy", "Okta"]
sched_url: https://kccnceu2025.sched.com/event/1txFe/do-your-containers-even-lift-a-hardening-guide-for-k8s-containers-cailyn-edwards-daniel-murphy-okta
youtube_search_url: https://www.youtube.com/results?search_query=Do+Your+Containers+Even+Lift+%E2%80%93+A+Hardening+Guide+for+K8s+Containers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Do Your Containers Even Lift – A Hardening Guide for K8s Containers - Cailyn Edwards & Daniel Murphy, Okta

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Cailyn Edwards, Daniel Murphy, Okta
- Schedule: https://kccnceu2025.sched.com/event/1txFe/do-your-containers-even-lift-a-hardening-guide-for-k8s-containers-cailyn-edwards-daniel-murphy-okta
- Busca YouTube: https://www.youtube.com/results?search_query=Do+Your+Containers+Even+Lift+%E2%80%93+A+Hardening+Guide+for+K8s+Containers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Do Your Containers Even Lift – A Hardening Guide for K8s Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFe/do-your-containers-even-lift-a-hardening-guide-for-k8s-containers-cailyn-edwards-daniel-murphy-okta
- YouTube search: https://www.youtube.com/results?search_query=Do+Your+Containers+Even+Lift+%E2%80%93+A+Hardening+Guide+for+K8s+Containers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lj_qgsb4h38
- YouTube title: Do Your Containers Even Lift – A Hardening Guide for K8s Containers - Cailyn Edwards & Daniel Murphy
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/do-your-containers-even-lift-a-hardening-guide-for-k8s-containers/lj_qgsb4h38.txt
- Transcript chars: 31267
- Keywords: security, container, images, secure, docker, application, latest, little, starting, running, default, cluster, create, policy, profile, containers, squishy, components

### Resumo baseado na transcript

So, before we get started today, Kayla's going to take a quick selfie with the audience. So, I would not have worn this outfit if I knew how many people were going to show up, but I'm here and I'm in it and I'm so happy to see you all. Starting off, because this is KubeCon, we'll go through the Kubernetes components. and a few terms that we're going to be using that are kind of container security specific. So these are just a specific type of tool that are designed to examine your container in some way to detect things like insecure configuration, things that look like they might be secret, vulnerable packages, that sort of thing. So by that I mean an exploit that can demonstrate that this thing is actually usable but has not been built to do something actively malicious like xfilling all of your credentials or starting up a crypto miner.

### Excerpt da transcript

Good afternoon, KubeCon. How are we doing? So, before we get started today, Kayla's going to take a quick selfie with the audience. That's all right. Ready? Okay. On three. Flex if you're up for it. Two. Three. Woo. I think maybe a little more. Woo! Woo! Woo! Awesome. All right. So, I would not have worn this outfit if I knew how many people were going to show up, but I'm here and I'm in it and I'm so happy to see you all. Thank you so much for taking the time on the last day of KubeCon in the afternoon to come to our talk. It means the world to us. So, what are we talking about? I assume this is why you're here. It's the title. It's funny. Um, and that's what we're going to go over. This is an entrylevel talk. um going over the risks of containers if you just make them and you don't necessarily know what you're making. So we will kick off with our introduction. We are your coaches. My name is Kayn Edwards. I am a security engineer at Ozero by Octa and also a co-chair of Kubernetes SIG Security, a CNCF ambassador, a very enthusiastic dog mom, and a Sander fan.

I've got my Bridgeport earrings on. If that's a reference you appreciate, then uh we should be friends. And I will pass it over to Dan to introduce himself. So my name is Daniel Murphy. I am also a senior security engineer at Oslo by Octa. I am a lover of photography, coffee, and outdoor adventures and also a massive sounder fan. Okay, so what are we going to go through today? We will start off going over the lingo. We're going to go over the what, the how, and the TLDDR. We all know that the Kubernetes landscape and the software landscape in general is full of overloaded terms. So, let's break them down. Oops. And make sure that we know what we're talking about. Next, we're going to go into the before. We're going to meet this soft and vulnerable container, get to know what they've got going on under the hood. Finally, we'll get into what you're all here for, which is the montage. We're going to take that container from squishy to strong. Uh, and then we'll finish off with coach's corner. We're going to offer some tips to take forward to your company, to your personal home project so that you can secure your containers and have rocksolid showworthy containers.

Finally, um I'll start with the lingo. As I said, we want to make sure that we're all jumping into this presentation with a shared understanding. If I say any words, I want to make sure that you are thinking of the same thing that I am think
