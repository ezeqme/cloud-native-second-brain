---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Bob Callaway", "Red Hat", "Dan Lorenc", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV1r/sigstore-how-we-started-where-we-are-where-we-are-headed-bob-callaway-red-hat-dan-lorenc-google
youtube_search_url: https://www.youtube.com/results?search_query=sigstore%3A+How+We+Started%2C+Where+We+Are%2C+Where+We+are+Headed+CNCF+KubeCon+2021
slides: []
status: parsed
---

# sigstore: How We Started, Where We Are, Where We are Headed - Bob Callaway, Red Hat & Dan Lorenc, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: United States / Los Angeles
- Speakers: Bob Callaway, Red Hat, Dan Lorenc, Google
- Schedule: https://kccncna2021.sched.com/event/lV1r/sigstore-how-we-started-where-we-are-where-we-are-headed-bob-callaway-red-hat-dan-lorenc-google
- Busca YouTube: https://www.youtube.com/results?search_query=sigstore%3A+How+We+Started%2C+Where+We+Are%2C+Where+We+are+Headed+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre sigstore: How We Started, Where We Are, Where We are Headed.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1r/sigstore-how-we-started-where-we-are-where-we-are-headed-bob-callaway-red-hat-dan-lorenc-google
- YouTube search: https://www.youtube.com/results?search_query=sigstore%3A+How+We+Started%2C+Where+We+Are%2C+Where+We+are+Headed+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PVhRQFS9Njg
- YouTube title: Sigstore: How We Started, Where We Are, Where We are Headed - Bob Callaway & Dan Lorenc
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sigstore-how-we-started-where-we-are-where-we-are-headed/PVhRQFS9Njg.txt
- Transcript chars: 41887
- Keywords: actually, transparency, certificate, signing, verify, signed, public, signature, github, logs, identity, container, itself, information, supply, google, commit, together

### Resumo baseado na transcript

all right let's get started thank you everybody for joining us today uh this talk is about six door sig store the past the present and the future my name is dan lawrence and up here is bob calloway and introduce yourself i'm bob calloway i'm a software engineer at red hat um working on various supply chain projects um also one of the uh members of the technical steering committee for sigstor awesome so thanks for joining us right before lunch today and delaying your lunch a little bit july and the transparency logs that it interacts with are going to move to beta any data um so here's some stats on the community the activity that we've seen it's really been amazing all of the support from everybody uh in advancing the c

### Excerpt da transcript

all right let's get started thank you everybody for joining us today uh this talk is about six door sig store the past the present and the future my name is dan lawrence and up here is bob calloway and introduce yourself i'm bob calloway i'm a software engineer at red hat um working on various supply chain projects um also one of the uh members of the technical steering committee for sigstor awesome so thanks for joining us right before lunch today and delaying your lunch a little bit we're gonna be talking about sig storage sig store is a new linux foundation project to help improve software supply chain security through transparency we're going to talk a little bit about supply chain security but this is one of like 100 talks about that topic this kubecon so i don't think we need to spend too much time on that uh was anybody here at supply chain security day a few days ago okay a lot of familiar faces here in the back uh we're gonna be going over the history of state store where it started uh a few it was earlier 2021 but uh yeah it feels like a couple months but it's been a long time now um some of the work we've done along the way and we're gonna do some demos showing how all the different components of stick store fit together and can be used with a couple real world examples relevant to kubecon we're going to cover some of the architecture there's some complicated uh hand wavy spaghetti drawings but we'll break them down piece by piece and show how they all fit together and then we'll talk about some of the work we have planned in cig store going forward so we have one slide here one obligatory one on supply chain security before we can move on a bunch of scary figures graphs going up and to the right these are both from the recent sona type report a 650 percent increase in software supply chain attacks and open source in these things aren't slowing down i think the eu predicted another 400 percent increase next year lots of attacks are happening this is very scary but thankfully a whole bunch of projects a whole bunch of people here at uh kubecon a whole bunch of people in the cloud native ecosystem are working on helping protect open source and protect software supply chains so like i said cycler's mission statement is to really help improve software supply chain transparency we're doing this through software signing and provenance when we originally started the sig store project we took a lot of inspiration from let's encrypt how many people here
