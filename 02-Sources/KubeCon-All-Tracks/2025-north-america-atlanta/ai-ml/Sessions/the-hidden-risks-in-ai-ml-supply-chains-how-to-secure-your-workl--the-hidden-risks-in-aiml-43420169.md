---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Security"]
speakers: ["Yash Pimple", "Chainguard"]
sched_url: https://kccncna2025.sched.com/event/27Fag/the-hidden-risks-in-aiml-supply-chains-how-to-secure-your-workloads-yash-pimple-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=The+Hidden+Risks+in+AI%2FML+Supply+Chains%3A+How+To+Secure+Your+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Hidden Risks in AI/ML Supply Chains: How To Secure Your Workloads - Yash Pimple, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Atlanta
- Speakers: Yash Pimple, Chainguard
- Schedule: https://kccncna2025.sched.com/event/27Fag/the-hidden-risks-in-aiml-supply-chains-how-to-secure-your-workloads-yash-pimple-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hidden+Risks+in+AI%2FML+Supply+Chains%3A+How+To+Secure+Your+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Hidden Risks in AI/ML Supply Chains: How To Secure Your Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fag/the-hidden-risks-in-aiml-supply-chains-how-to-secure-your-workloads-yash-pimple-chainguard
- YouTube search: https://www.youtube.com/results?search_query=The+Hidden+Risks+in+AI%2FML+Supply+Chains%3A+How+To+Secure+Your+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3lcyFfA1Wbk
- YouTube title: The Hidden Risks in AI/ML Supply Chains: How To Secure Your Workloads - Yash Pimple, Chainguard
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-hidden-risks-in-ai-ml-supply-chains-how-to-secure-your-workloads/3lcyFfA1Wbk.txt
- Transcript chars: 31046
- Keywords: basically, particular, supply, around, entire, source, further, coming, whenever, dependency, provide, attack, models, working, pickle, signing, software, towards

### Resumo baseado na transcript

So today I will be talking about the hidden risks within the AML supply chain and how we can secure them and the tools that have been currently been worked upon within the opensource community. I'm currently working as an associate software engineer with chain guard. So whenever uh has a user if I'm trying to use that particular model I can validate and make sure it's coming it has all the I can say pre-check security measure that have been taken to basically get delivered to us and this is where that particular I can say uh CV or I can say problem is for example this is how it tends to look like. that is basically used to sign a model and that particular data I can say logs are further sent to uh 62 transparency log in this case it's record it's kind of a data it's not a database you can refer it as a database where all the logs are basically stored so anyone if even if I sign that particular model and if you want to check you can go through that transparency logs inside the record and find out each thing so it's kind of a way you

### Excerpt da transcript

Let's dive into my talk. So today I will be talking about the hidden risks within the AML supply chain and how we can secure them and the tools that have been currently been worked upon within the opensource community. And that's that's the entire overview of the talk. So before getting started a bit about myself hello everyone myself. I'm currently working as an associate software engineer with chain guard. uh we are the team who basically work towards providing zero CV free hardet container images and addition to that I'm also a CNF ambassador and an AWS committee builder in my free time I like to talk about I like to build like play around cage I mean a way of building my like own home lab setup so if you have something to chat about that happy to have a discussion around that so yeah this is a talk overview we will be going through and understanding how does the how does an AMS supply chain tends to look like how it's different to a traditional supply chain uh what's the current threat landscape and attack surface for the entire supply chain uh around this and kind of tools and strategies to understanding how we can basically tackle and try to work around fixing the like preventing the attack surface which are present and some final thoughts.

So the reason we are here because it's like in the past 3 to four year there has been plenty like significant rise of supply chain attacks uh and one of the major eye awakening attack was like solar wind which happened in 2020 that was like a complete I can say uh a way a time where basically everyone started thinking security to be one of the critical and utmost thing and everyone started working towards finding out and fix creating solutions around fixing this particular problem. uh there are plenty of I can say supply chain attacks I have listed over here uh starting from ly file which was like an attack that happened because of uh like maintainers uh key which got exposed and apart from apart from that there are plenty of more and it it's it's keep on increasing there is no way attackers will like try to like stop there there will be more attacks which are ongoing and they have been increasing in the order of as we speak over here So what does a traditional software supply chain tends to look like?

We have a developer, we have a source code and we basically that particular source code is basically used to build artifacts. Uh at the time of building or building artifacts, we make use of third party dependency
