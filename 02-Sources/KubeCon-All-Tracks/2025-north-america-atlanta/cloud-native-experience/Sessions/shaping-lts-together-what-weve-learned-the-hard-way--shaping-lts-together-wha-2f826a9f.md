---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Experience"
themes: ["Cloud Native Experience"]
speakers: ["Nikhita Raghunath", "Nikhila Kamath", "Broadcom", "Micah Hausler", "AWS", "Jeremy Rickard", "Microsoft", "Aniket Ponkshe", "Canonical"]
sched_url: https://kccncna2025.sched.com/event/27FWW/shaping-lts-together-what-weve-learned-the-hard-way-nikhita-raghunath-nikhila-kamath-broadcom-micah-hausler-aws-jeremy-rickard-microsoft-aniket-ponkshe-canonical
youtube_search_url: https://www.youtube.com/results?search_query=Shaping+LTS+Together%3A+What+We%E2%80%99ve+Learned+the+Hard+Way+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Shaping LTS Together: What We’ve Learned the Hard Way - Nikhita Raghunath & Nikhila Kamath, Broadcom; Micah Hausler, AWS; Jeremy Rickard, Microsoft; Aniket Ponkshe, Canonical

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Cloud Native Experience]]
- País/cidade: United States / Atlanta
- Speakers: Nikhita Raghunath, Nikhila Kamath, Broadcom, Micah Hausler, AWS, Jeremy Rickard, Microsoft, Aniket Ponkshe, Canonical
- Schedule: https://kccncna2025.sched.com/event/27FWW/shaping-lts-together-what-weve-learned-the-hard-way-nikhita-raghunath-nikhila-kamath-broadcom-micah-hausler-aws-jeremy-rickard-microsoft-aniket-ponkshe-canonical
- Busca YouTube: https://www.youtube.com/results?search_query=Shaping+LTS+Together%3A+What+We%E2%80%99ve+Learned+the+Hard+Way+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Shaping LTS Together: What We’ve Learned the Hard Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWW/shaping-lts-together-what-weve-learned-the-hard-way-nikhita-raghunath-nikhila-kamath-broadcom-micah-hausler-aws-jeremy-rickard-microsoft-aniket-ponkshe-canonical
- YouTube search: https://www.youtube.com/results?search_query=Shaping+LTS+Together%3A+What+We%E2%80%99ve+Learned+the+Hard+Way+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=z5152J_nFmw
- YouTube title: Shaping LTS Together: What We’ve Learned the... Nikhita R, Nikhila K, Micah H, Jeremy R & Aniket P
- Match score: 0.785
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/shaping-lts-together-what-weve-learned-the-hard-way/z5152J_nFmw.txt
- Transcript chars: 27105
- Keywords: support, upgrade, customers, release, version, working, actually, another, releases, everyone, vendors, probably, upstream, around, longer, versions, long-term, feature

### Resumo baseado na transcript

Uh I'm I'm generally excited about this conversation because the timing couldn't be more interesting. Uh as some of you may know, so the Kubernetes LTS working group uh has proposed to wind down. I'm a product manager at uh Broadcom uh mainly focused on uh Kubernetes and LTS being one of the main focus. I am a principal engineer at Microsoft and I lead a team that's responsible for building um artifacts that are going to get consumed inside of Azure services like AKS uh specifically around Kubernetes. I think another factor that comes into this for some sets of users is remembering the past and there were certain periods of time where upgrading Kubernetes was extremely difficult. Uh you know certain APIs might have gone away or there were significant changes that were really hard to react to especially if you built custom solutions on top of Kubernetes.

### Excerpt da transcript

Hi everyone. Thanks for joining the panel on shaping LTS together. What we've learned the hard way. Uh I'm I'm generally excited about this conversation because the timing couldn't be more interesting. Uh as some of you may know, so the Kubernetes LTS working group uh has proposed to wind down. Uh so this is an interesting time to have this conversation and have this panel in the first place. uh but even though the working group has decided to wrap up uh the problems that it's trying to solve hasn't going away right so I think it's uh timely that we talk about it and uh who better to talk about it than the people who are actually doing this in the real world uh so uh just just a quick note about that though so we not going to be comparing vendors or declaring that this is the best model to do LT LTS. This is more about just sharing the common challenges uh patterns that we've seen while doing LTS in our respective companies or just in the community and what can we take away from it in the ecosystem.

Uh so with that I'll let the panelists introduce themselves and maybe I'll I'll go first just since I'm speaking. Um so my name is Nikita. Uh I'll be the moderator for the session. Uh I am an engineering manager at Broadcom. Uh and I do all things Kubernetes. >> And I'm uh Micah Hler. I uh am a principal engineer at AWS. I work on Kubernetes and EKS primarily on security but also have quite a bit of overlap with LTS. I'm also uh one of the co-chairs of the LTS working group. >> Uh hello everyone. Uh I'm Nicola. I'm a product manager at uh Broadcom uh mainly focused on uh Kubernetes and LTS being one of the main focus. Hi everyone, I'm Anik Pongche. Um I'm at Canonical Ubuntu. Uh I've had the privilege to run our partnership uh with many different companies including VMware. In my past I've run uh Nvidia and other relationships. Happy to be here and excited about this chat. Hey everybody, thanks for coming. My name is Jeremy Rickard. I am a principal engineer at Microsoft and I lead a team that's responsible for building um artifacts that are going to get consumed inside of Azure services like AKS uh specifically around Kubernetes.

I'm also a co-chair of working group LTS and a co-chair of sik release. >> Thanks everyone. So let's kick it off. Um so let's start with really understanding why LTS, right? like what so what's really driving this conversation in the industry and why should we care about it? Anyone wants to go first? >> Okay, I can go first. Um yeah
