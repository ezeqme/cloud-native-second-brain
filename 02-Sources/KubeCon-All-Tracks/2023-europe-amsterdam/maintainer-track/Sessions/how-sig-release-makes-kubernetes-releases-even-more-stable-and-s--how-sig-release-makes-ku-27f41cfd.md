---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Veronica Lopez", "PlanetScale", "Marko Mudrinić", "Kubermatic GmbH"]
sched_url: https://kccnceu2023.sched.com/event/1HyUA/how-sig-release-makes-kubernetes-releases-even-more-stable-and-secure-veronica-lopez-planetscale-marko-mudrinic-kubermatic-gmbh
youtube_search_url: https://www.youtube.com/results?search_query=How+SIG+Release+Makes+Kubernetes+Releases+Even+More+Stable+and+Secure+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How SIG Release Makes Kubernetes Releases Even More Stable and Secure - Veronica Lopez, PlanetScale & Marko Mudrinić, Kubermatic GmbH

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Veronica Lopez, PlanetScale, Marko Mudrinić, Kubermatic GmbH
- Schedule: https://kccnceu2023.sched.com/event/1HyUA/how-sig-release-makes-kubernetes-releases-even-more-stable-and-secure-veronica-lopez-planetscale-marko-mudrinic-kubermatic-gmbh
- Busca YouTube: https://www.youtube.com/results?search_query=How+SIG+Release+Makes+Kubernetes+Releases+Even+More+Stable+and+Secure+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How SIG Release Makes Kubernetes Releases Even More Stable and Secure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyUA/how-sig-release-makes-kubernetes-releases-even-more-stable-and-secure-veronica-lopez-planetscale-marko-mudrinic-kubermatic-gmbh
- YouTube search: https://www.youtube.com/results?search_query=How+SIG+Release+Makes+Kubernetes+Releases+Even+More+Stable+and+Secure+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AP9G5Jtn9y4
- YouTube title: How SIG Release Makes Kubernetes Releases Even More Stable & Secure- Veronica Lopez & Marko Mudrinić
- Match score: 0.878
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-sig-release-makes-kubernetes-releases-even-more-stable-and-secure/AP9G5Jtn9y4.txt
- Transcript chars: 28135
- Keywords: release, packages, change, releases, secure, google, images, basically, changes, already, credits, little, especially, issues, working, eventually, access, manager

### Resumo baseado na transcript

well welcome thank you so much for being here um this is our talk about how sick release makes kubernetes releases even more stable and secure hopefully my name is Veronica Lopez I'm Tech lead for sick release and I also work at Planet scale uh the company behind BTS okay everyone thank you for coming today I am Marco modernich I am a senior software engineer at kubermatic I am a release manager for the kubernetes project a long time Sig release contributor and we are definitely happy to and many other six in the community as well as individual contributors and it is about register changes as you may know we introduced the registicated as IO at kubecon n a last year is a new frontal for all kubernetes images and as a this was the uh supported the final supporter release at that time so we backboarded this change for all those supported releases at that time uh why it is a problem because as per our rules and how we defined it you can only backboard updates on blog and stuff like that so that you are aware of it now we are coming to an end how to get evolving Sig release you can always reach out to us on single list Channel or kubernetes slack we also have our

### Excerpt da transcript

well welcome thank you so much for being here um this is our talk about how sick release makes kubernetes releases even more stable and secure hopefully my name is Veronica Lopez I'm Tech lead for sick release and I also work at Planet scale uh the company behind BTS okay everyone thank you for coming today I am Marco modernich I am a senior software engineer at kubermatic I am a release manager for the kubernetes project a long time Sig release contributor and we are definitely happy to see you all today let's get started yay okay so this is our agenda for today um a little bit of a sick release introduction for those of you who are not familiar with it a bit over the release team then about the supply chain security uh registry changes that I'm sure a lot of you are a bit familiar with that and last but not least the packages they are RPM and WM packages and yeah so let's get started welcome to Sig release uh if you've been to or previous talks you might already be familiar with what we do but if you don't uh the quick recap is uh sick really is a group responsible for ensuring quality kubernetes releases this means a lot of things uh this includes managing the releases uh from end to end uh following the progress of our release cycle guiding contributors along the way but also maintaining tooling uh needed to to release kubernetes this is very important because if you're a release manager or or a release engineer for any other project either open source or internally you might use other tools that are available for free or paid whatever but are that are already available but we build our own tools so this has many implications that we will mention along the talk and but we're a self-service team we don't just produce the releases but we do the the the we're on the show behind that and well also Sig release ensures that each release is stable reliable on time and secure and especially with so many collaborators from different companies and individual contributors Etc and of course this wouldn't be possible if we didn't work in collaboration with other six so the latest uh kubernetes release is uh 127 called Chill Vibes if you know sander you understand this Vibe uh sander was the lead of kubernetes 127 and it's the first release of 2023 with 60 enhancements 18 on Alpha 29 on beta and 13 unstable and the release team is a sub team under seek release I know that a lot of people are confused about is like who is the earliest team who's strict release um Etc
