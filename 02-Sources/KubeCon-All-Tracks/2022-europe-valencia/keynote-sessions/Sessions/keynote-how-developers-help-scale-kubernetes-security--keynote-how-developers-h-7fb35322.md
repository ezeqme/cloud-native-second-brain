---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Keynote Sessions"
themes: ["Security", "Kubernetes Core", "SRE Reliability"]
speakers: ["Connor Gorman", "Senior Principal Software Engineer", "Red Hat"]
sched_url: https://kccnceu2022.sched.com/event/yuGl/keynote-how-developers-help-scale-kubernetes-security-connor-gorman-senior-principal-software-engineer-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+How%C2%A0Developers%C2%A0Help%C2%A0Scale%C2%A0Kubernetes%C2%A0Security+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Keynote: How Developers Help Scale Kubernetes Security - Connor Gorman, Senior Principal Software Engineer, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Security]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Connor Gorman, Senior Principal Software Engineer, Red Hat
- Schedule: https://kccnceu2022.sched.com/event/yuGl/keynote-how-developers-help-scale-kubernetes-security-connor-gorman-senior-principal-software-engineer-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+How%C2%A0Developers%C2%A0Help%C2%A0Scale%C2%A0Kubernetes%C2%A0Security+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Keynote: How Developers Help Scale Kubernetes Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yuGl/keynote-how-developers-help-scale-kubernetes-security-connor-gorman-senior-principal-software-engineer-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+How%C2%A0Developers%C2%A0Help%C2%A0Scale%C2%A0Kubernetes%C2%A0Security+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zxPYK6O2sg0
- YouTube title: Keynote: How Developers Help Scale Kubernetes Security - Connor Gorman, Red Hat
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/keynote-how-developers-help-scale-kubernetes-security/zxPYK6O2sg0.txt
- Transcript chars: 4117
- Keywords: security, developers, vulnerability, number, critical, probably, applications, organizations, issues, everyone, overwhelming, success, ecosystem, deployments, engineers, trying, potentially, quickly

### Resumo baseado na transcript

hey everyone thank you for being here i'm conor gorman i'm a senior principal engineer at red hat and for the last five years i've worked on the stack rocks project which is now open source it's a kubernetes security platform so it's pretty fitting today that i'm going to talk to you about how developers help scale kubernetes security maybe there we go awesome at the end of 2021 in a report for the cncf it was said that 5.6 million developers use kubernetes that number has probably grown

### Excerpt da transcript

hey everyone thank you for being here i'm conor gorman i'm a senior principal engineer at red hat and for the last five years i've worked on the stack rocks project which is now open source it's a kubernetes security platform so it's pretty fitting today that i'm going to talk to you about how developers help scale kubernetes security maybe there we go awesome at the end of 2021 in a report for the cncf it was said that 5.6 million developers use kubernetes that number has probably grown a lot by today and it also tells it speaks to me about the overwhelming success of kubernetes but also the overwhelming success of the ecosystem and the communities that we've built we've enabled developers to ship more code build more deployments build more applications and ship faster than ever before but there are security implications to this change largely that the number of developers is greatly larger than the number of security engineers and so we have small security teams tasked with trying to support this ever-growing number of deployments excuse me this is probably best shown through something like log for shell this is a sneak peek into many organizations including myself and security engineers and developers rapidly trying to fix log for shell for those of you who may not know block for shell is a critical vulnerability in the log for j logging library and it was rated attend by apache the most critical vulnerability and would allow an attacker to potentially run malicious code against your infrastructure what happened though and what it made people do is make people come together it made both developers and security teams quickly collaborate to figure out which applications were vulnerable where those applications were deployed and how quickly you could submit a patch log for shell isn't the first critical vulnerability and it certainly won't be the last vulnerability so really how can we make this collaboration permanent and how how can we prepare our organizations for the next one the answer really lies in leveraging the developer ecosystem that made this possible in the first place right how do we get developers deliver software so fast it's never too early to bake in security whether you're in an ide you know updating a package like log4j whether you're building an image in ci with a tool like tekton or you're continuously deploying with a tool like argo cd you know straight to production the real goal is to involve developers as early as possible in secu
