---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Community"
themes: ["AI ML", "Kubernetes Core", "Sustainability", "Community Governance"]
speakers: ["Nabarun Pal", "Madhav Jivrajani", "VMware"]
sched_url: https://kccnceu2023.sched.com/event/1HyeH/wildfires-firefighters-and-sustainability-learnings-from-mitigating-kubernetes-fires-in-the-community-nabarun-pal-madhav-jivrajani-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Wildfires%2C+Firefighters+and+Sustainability+-+Learnings+from+Mitigating+Kubernetes+Fires+in+the+Community+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Wildfires, Firefighters and Sustainability - Learnings from Mitigating Kubernetes Fires in the Community - Nabarun Pal & Madhav Jivrajani, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Community]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Sustainability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nabarun Pal, Madhav Jivrajani, VMware
- Schedule: https://kccnceu2023.sched.com/event/1HyeH/wildfires-firefighters-and-sustainability-learnings-from-mitigating-kubernetes-fires-in-the-community-nabarun-pal-madhav-jivrajani-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Wildfires%2C+Firefighters+and+Sustainability+-+Learnings+from+Mitigating+Kubernetes+Fires+in+the+Community+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Wildfires, Firefighters and Sustainability - Learnings from Mitigating Kubernetes Fires in the Community.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyeH/wildfires-firefighters-and-sustainability-learnings-from-mitigating-kubernetes-fires-in-the-community-nabarun-pal-madhav-jivrajani-vmware
- YouTube search: https://www.youtube.com/results?search_query=Wildfires%2C+Firefighters+and+Sustainability+-+Learnings+from+Mitigating+Kubernetes+Fires+in+the+Community+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mcBp63qoXpE
- YouTube title: Wildfires, Firefighters and Sustainability - Learnings from... - Nabarun Pal & Madhav Jivrajani
- Match score: 0.779
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/wildfires-firefighters-and-sustainability-learnings-from-mitigating-ku/mcBp63qoXpE.txt
- Transcript chars: 31280
- Keywords: release, firefighters, basically, releases, happen, triage, actually, reliability, across, collaboration, essentially, blockers, happened, wildfires, almost, freeze, issues, require

### Resumo baseado na transcript

hey everyone uh is the volume fine can you all hear me it's good okay thank you um Welcome to our talk on wildfires firefighting and how we keep kubernetes releases reliable and on time um I am Navarone uh hi I'm madhav we both work at VMware so before we begin our talk some golden rules from the community uh please follow the code of conduct which essentially boils down to please be kind and respectful to everyone and don't do or say anything that you might regret because

### Excerpt da transcript

hey everyone uh is the volume fine can you all hear me it's good okay thank you um Welcome to our talk on wildfires firefighting and how we keep kubernetes releases reliable and on time um I am Navarone uh hi I'm madhav we both work at VMware so before we begin our talk some golden rules from the community uh please follow the code of conduct which essentially boils down to please be kind and respectful to everyone and don't do or say anything that you might regret because everything is being recorded I do it almost every day in my community meeting so uh for the virtual audience we do have closed captioning so if you are watching it online please do enable that now who are we um uh I'm a mother I work as an engineer at VMware I'm also a technical lead of say contributor experience if you don't know what that is it's a special interest group within the kubernetes community and um yeah I'm one of the kubernetes training committee members and I am also a kubernetes sick country back chair and I do a lot of kubernetes security stuff ah before we start um to whoever uses kubernetes please start using registry.kats.io kts.gc.io is Frozen now and it would soon go away you won't be able to access the registry anymore I mean we have been talking about this probably thousand times uh in the conference before the conference I hope like you have already moved out uh but still uh good thing to call out now what's the agenda uh we will show you how kubernetes releases happen then we will go to set some context on why we are giving this talk we will talk about what goes right when we try to fix fires in the community what can we improve and what you can take away from this talk for your projects so to start with uh how is kubernetes released when is kubernetes released so we release kubernetes every four months we do approximately three releases a year and it's an very elaborate song and dance of people and processes and there's a big mix of both now about the people we have a really uh big yet small team we are always short of hands but we do have some verticals in the release team who handle like some specific areas of the release uh the release lead is basically the coordinator for everyone uh branch manager Cuts tags uh the bacteriach team does triage uh say signal team takes care of our CI comms team writes basically the blogs that you see at the end of the release the feature block the release Blog the docs team handles all the docs that users consume the announce
