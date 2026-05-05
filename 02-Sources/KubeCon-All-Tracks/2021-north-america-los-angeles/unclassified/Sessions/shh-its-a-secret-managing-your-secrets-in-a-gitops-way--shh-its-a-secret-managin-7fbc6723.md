---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Unclassified"
themes: ["GitOps Delivery"]
speakers: ["Jake Wernette", "Josh Kayani", "IBM"]
sched_url: https://kccncna2021.sched.com/event/lV07/shh-its-a-secret-managing-your-secrets-in-a-gitops-way-jake-wernette-josh-kayani-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Shh%2C+It%E2%80%99s+a+Secret%3A+Managing+Your+Secrets+in+a+GitOps+Way+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Shh, It’s a Secret: Managing Your Secrets in a GitOps Way - Jake Wernette & Josh Kayani, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Los Angeles
- Speakers: Jake Wernette, Josh Kayani, IBM
- Schedule: https://kccncna2021.sched.com/event/lV07/shh-its-a-secret-managing-your-secrets-in-a-gitops-way-jake-wernette-josh-kayani-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Shh%2C+It%E2%80%99s+a+Secret%3A+Managing+Your+Secrets+in+a+GitOps+Way+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Shh, It’s a Secret: Managing Your Secrets in a GitOps Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV07/shh-its-a-secret-managing-your-secrets-in-a-gitops-way-jake-wernette-josh-kayani-ibm
- YouTube search: https://www.youtube.com/results?search_query=Shh%2C+It%E2%80%99s+a+Secret%3A+Managing+Your+Secrets+in+a+GitOps+Way+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7L6nSuKbC2c
- YouTube title: Shh, It’s a Secret: Managing Your Secrets in a GitOps Way - Jake Wernette & Josh Kayani, IBM
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/shh-its-a-secret-managing-your-secrets-in-a-gitops-way/7L6nSuKbC2c.txt
- Transcript chars: 34284
- Keywords: argo, secret, basically, secrets, cluster, actually, plugin, wanted, deploy, server, instance, config, custom, little, password, plug-in, resources, manager

### Resumo baseado na transcript

yeah thanks for the intro um like you said i'm jake this is josh um we're so reliability engineers at ibm and today we're going to talk about how we are managing our secrets via githubs so uh i already got a good intro but just a little bit more background i'm from michigan a very small town in michigan and i graduated from central michigan university with a computer science degree i started my career at ibm i went to red hat for a little bit and then i

### Excerpt da transcript

yeah thanks for the intro um like you said i'm jake this is josh um we're so reliability engineers at ibm and today we're going to talk about how we are managing our secrets via githubs so uh i already got a good intro but just a little bit more background i'm from michigan a very small town in michigan and i graduated from central michigan university with a computer science degree i started my career at ibm i went to red hat for a little bit and then i came back to ibm um as an sre um just a couple years ago um some things that i'm really into um like argo cd like you mentioned cloud native terraform operators and customer resources and stuff like that yeah and i'm josh you know i'm uh been here since uh 2018 may 2018 at ibm from nc state university over in raleigh north carolina and i'm just happy to be here so yeah all right so a little bit of background um just to talk about our journey into kubernetes so um the team that we are on we started out managing just um supporting just one development team that was um that had this big monolith um that was deployed to websphere now sorry about that um and everything was being done manual you know when the time was right we had these jars and we just manually deployed them to the server um so and all that setup was done manually just by a small team of just a few but that monolith started to grow and started to get slow um performance started to suffer so we decided let's look at you know breaking this up into microservices and look for a platform as a service that's where we went into public cloud with cloud foundry um and this worked really nice because we were able to you know break up the monolith but being a small team um it did become a little cumbersome especially as we got more um developers under our support so it went from just you know one application with these microservices to two three four five applications um and all their separate micro services and so it was becoming hard to orchestrate them right um so that is where kubernetes came into we wanted to use kubernetes to help simplify this process um which simplify and not simplify but um you know it helped orchestrate these and um these different applications and helped us you know to be a small team and manage multiple uh developer teams but with that um we did notice you know a lot more resources there's a lot more managing with these clusters um you know a lot of these resources that were necessary to be there for these applications full sec
