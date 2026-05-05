---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Jim Bugwadia", "Nirmata", "Andy Suderman", "Fairwinds"]
sched_url: https://kccnceu2024.sched.com/event/1YhhD/kubernetes-policy-time-machine-where-to-next-jim-bugwadia-nirmata-andy-suderman-fairwinds
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Policy+Time+Machine%3A+Where+to+Next%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Policy Time Machine: Where to Next? - Jim Bugwadia, Nirmata & Andy Suderman, Fairwinds

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Jim Bugwadia, Nirmata, Andy Suderman, Fairwinds
- Schedule: https://kccnceu2024.sched.com/event/1YhhD/kubernetes-policy-time-machine-where-to-next-jim-bugwadia-nirmata-andy-suderman-fairwinds
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Policy+Time+Machine%3A+Where+to+Next%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Policy Time Machine: Where to Next?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhhD/kubernetes-policy-time-machine-where-to-next-jim-bugwadia-nirmata-andy-suderman-fairwinds
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Policy+Time+Machine%3A+Where+to+Next%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=apYGi-R28MU
- YouTube title: Kubernetes Policy Time Machine: Where to Next? - Jim Bugwadia, Nirmata & Andy Suderman, Fairwinds
- Match score: 0.742
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-policy-time-machine-where-to-next/apYGi-R28MU.txt
- Transcript chars: 32637
- Keywords: policy, admission, policies, validating, security, working, dynamic, server, controllers, little, course, manage, checks, configuration, objects, write, started, within

### Resumo baseado na transcript

good afternoon everyone and thank you for joining us uh so for the next 30 minutes we're going to talk about kubernetes policy management uh so really excited to cover uh you know and we have quite a lot of topics prepared so we're going to start with some quick introductions talk about why you need policies in kubernetes what kubernetes policies are what types of policies are supported then we're going to go into some details about you know specific policy implementations in including pod security admissions um or

### Excerpt da transcript

good afternoon everyone and thank you for joining us uh so for the next 30 minutes we're going to talk about kubernetes policy management uh so really excited to cover uh you know and we have quite a lot of topics prepared so we're going to start with some quick introductions talk about why you need policies in kubernetes what kubernetes policies are what types of policies are supported then we're going to go into some details about you know specific policy implementations in including pod security admissions um or uh for also like talk a little bit about PSPs why they were deprecated and then go into validating admission policies which is a new type in kubernetes compare that with what dynamic admission controllers can do uh and also introduce cell which is the language used by validating admission policies so quite a lot of topics to cover and we'll go through these and of course we'll try and save some time for questions and answers so happy to have the conversation um so to start off with just some quick introductions on who we are and why we care about this uh subject so I'm Jim badia co-founder CEO at nirmata I'm a co-chair in the policy working group within cncf also a maintainer on the cerno project which is a cncf policy engine and I'm Andy I'm the CTO at Fairwinds uh I've been working in the cloud native space for about 8 to 10 years at this point I'm a maintainer of several open source projects that you may be familiar with Goldilocks Pluto Polaris and uh also a co-chair of the policy working group as of late last year all right so just to kick things off introducing what we do in the policy working group and this is a community Forum everybody's welcome to join we have bi-weekly meetings so the charter of the working group is to define or at least catalog architectures different policy implementation types and and provide some guidance on what users should use right so we've done things like the policy reporting API is one of the initiatives that came out of the policy working group there's a number of different producers and consumers including cerno Falco trivy all of them can report policy results in a common structured Manner and we're looking at other initiatives as we move forward including like you know of course white papers things like we can do to help out again educate or inform the community um so starting with what is a policy right so there's a definition and one of the things we contributed from the working group there's a chapte
