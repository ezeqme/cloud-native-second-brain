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
themes: ["Security", "Kubernetes Core"]
speakers: ["Michele Chubirka", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7ri/why-perfect-compliance-is-the-enemy-of-good-kubernetes-security-michele-chubirka-google
youtube_search_url: https://www.youtube.com/results?search_query=Why+Perfect+Compliance+Is+the+Enemy+of+Good+Kubernetes+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Why Perfect Compliance Is the Enemy of Good Kubernetes Security - Michele Chubirka, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Michele Chubirka, Google
- Schedule: https://kccncna2024.sched.com/event/1i7ri/why-perfect-compliance-is-the-enemy-of-good-kubernetes-security-michele-chubirka-google
- Busca YouTube: https://www.youtube.com/results?search_query=Why+Perfect+Compliance+Is+the+Enemy+of+Good+Kubernetes+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Why Perfect Compliance Is the Enemy of Good Kubernetes Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ri/why-perfect-compliance-is-the-enemy-of-good-kubernetes-security-michele-chubirka-google
- YouTube search: https://www.youtube.com/results?search_query=Why+Perfect+Compliance+Is+the+Enemy+of+Good+Kubernetes+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TMZA4y9hslU
- YouTube title: Why Perfect Compliance Is the Enemy of Good Kubernetes Security - Michele Chubirka, Google
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/why-perfect-compliance-is-the-enemy-of-good-kubernetes-security/TMZA4y9hslU.txt
- Transcript chars: 41974
- Keywords: security, container, control, platform, remember, compliance, principles, controls, happens, privilege, threat, probably, actually, organization, figure, complex, application, separate

### Resumo baseado na transcript

why perfect compliance is the enemy of good kubernetes security I all I have regretted that title so many times you know when I rehearse the talk because it's really a mouthful say it like five times really fast I'm Michelle chab burka I'm A Cloud security Advocate at Google and I really do appreciate you being here because this is like one of the last sessions of the day and it shows real commitment to kubernetes security okay I just want to let you know I'm not going to

### Excerpt da transcript

why perfect compliance is the enemy of good kubernetes security I all I have regretted that title so many times you know when I rehearse the talk because it's really a mouthful say it like five times really fast I'm Michelle chab burka I'm A Cloud security Advocate at Google and I really do appreciate you being here because this is like one of the last sessions of the day and it shows real commitment to kubernetes security okay I just want to let you know I'm not going to go into nauseating EXC appreciating detail about kubernetes controls you've probably seen a lot of those talks here today or over the last few days um and there are lots of great books and and blogs and websites I'm really going to focus on um architecture principles because I think that's where you get a lot of bang for your buck and guess what I'm an ex architect so compliance I know I know overwhelming right all these different this is just a few of them right all these different standards and Frameworks how many people have to deal with regulatory Frameworks like Bank Frameworks oh yeah PCI DSS do we have any of those in here oh yep got some PCI great nist n yep okay cool cool cool cool okay I have circled the center for Internet Security CIS benchmarks because that's probably what everybody has to deal with the most right um you know that's what the dashboards and all the commercial tools actually use cubench uses the CIS benchmarks um for kubernetes uh like most of the cnap all the cspm tools they use uh the CIS kubernetes benchmarks under the hood and what's great about it is it's this great uh uh organization it's a nonprofit organization that brings uh vendors or open source um product teams with the community and they Advocate to come up with hardening standards right right now I don't recommend you read the the benchmarks yourself unless you have insomnia because like the kubernetes one is about 300 pages but you get the idea um this is really I'm going to teach you how to crack compliance not by gaming it but really compliance should be a continuous kind of improvement exercise right um it's never really done you don't just do it and then you're like hey I'm PCI it's always continuous you got to come back back to it every year but in theory you should be trying to work on it as you're going through um the maintenance on your platform your kubernetes platform that's what's going to make you successful okay I'm going to tldr this for you but if you want to take pictures of the q
