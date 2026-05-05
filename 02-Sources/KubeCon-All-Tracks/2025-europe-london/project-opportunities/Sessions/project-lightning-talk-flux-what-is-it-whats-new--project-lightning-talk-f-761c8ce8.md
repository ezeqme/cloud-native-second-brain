---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Tamao Nakahara", "Community Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcwa/project-lightning-talk-flux-what-is-it-whats-new-tamao-nakahara-community-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Flux+-+What+is+it+%26+What%27s+New%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Flux - What is it & What's New? - Tamao Nakahara, Community Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Tamao Nakahara, Community Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcwa/project-lightning-talk-flux-what-is-it-whats-new-tamao-nakahara-community-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Flux+-+What+is+it+%26+What%27s+New%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Flux - What is it & What's New?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwa/project-lightning-talk-flux-what-is-it-whats-new-tamao-nakahara-community-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Flux+-+What+is+it+%26+What%27s+New%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=k7Wcd9HdXAY
- YouTube title: Project Lightning Talk: Flux - What is it & What's New? - Tamao Nakahara, Community Maintainer
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-flux-what-is-it-whats-new/k7Wcd9HdXAY.txt
- Transcript chars: 6140
- Keywords: flux, security, excited, information, hopefully, design, multicluster, mention, cubecon, lightning, graduated, maintainers, become, standard, progressive, delivery, deployments, important

### Resumo baseado na transcript

My name is Tommo Nakahara and I'm one of the Flux community maintainers and I also work for a company called Helix that is a Flux user. So, Flux addresses many needs that hopefully have become standard by today that you expect out of your CI/CD system. And we've been really proud to have so many different types of enterprises that rely on Flux's design. Um and we love hearing uh stories for example about how they can rely on Flux to actually um speed up their Kubernetes adoption. So whether you're brand new to Kubernetes or you're somewhere in your journey um especially the progressive delivery that's um been there. We've had Flux users say like we really recommend that you make sure you install it as well because you know that you have a safety net to really experiment and try and have your various teams get used to Kubernetes itself.

### Excerpt da transcript

Great. So, I'm here to talk about the Flux project. Um, it is a graduated project in the CNCF. My name is Tommo Nakahara and I'm one of the Flux community maintainers and I also work for a company called Helix that is a Flux user. So, Flux addresses many needs that hopefully have become standard by today that you expect out of your CI/CD system. uh githops now is hopefully become a industry standard term and part of that is progressive delivery that flux also delivers that are like canary deployments, blue green deployments and such. Uh automation is really important. Uh you no longer want to be futing with um uh you know uh configs or um stuff that you've co uh cobbled together. And um you want to be able to rely on your system uh to be able to um you know deploy in the way that you need. Um reliability is important. Hopefully by now you've heard of Dora metrics which are metrics for you to be able to reliably release at the in the speed that you need to meet your business needs. Um security I'll talk a little bit more about this as well.

Um Flux has been designed to be security first. Um and scale. We've been really excited to have Telos and other companies that have pushed the limits of Flux design to meet their scale needs. So, uh, Flux is what created GitOps and we've been around for a while. We've been a graduated project. And so, a lot of times you might not even know if you're using GitOps with, um, Azure or AWS or one of the clouds. A lot of times Flux is what's under the hood. And we've been really proud to have so many different types of enterprises that rely on Flux's design. Um so I'll share some of the basics. For example, um it works with your existing infrastructure. Um and we love hearing uh stories for example about how they can rely on Flux to actually um speed up their Kubernetes adoption. So whether you're brand new to Kubernetes or you're somewhere in your journey um especially the progressive delivery that's um been there. We've had Flux users say like we really recommend that you make sure you install it as well because you know that you have a safety net to really experiment and try and have your various teams get used to Kubernetes itself.

Um so Flux is light uh fast and lightweight. Uh that's one of the things that we continue to get great feedback and one of the reasons for that people are really excited is that um Flux uses a native Helm SDK. Um that means that for example if you're using um Helm charts you're not you're not
