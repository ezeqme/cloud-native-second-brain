---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Application + Delivery"
themes: ["GitOps Delivery", "SRE Reliability"]
speakers: ["Wim Henderickx", "Nokia"]
sched_url: https://kccnceu2023.sched.com/event/1HydY/collaboratively-building-app-manifests-at-scale-in-complex-organizations-wim-henderickx-nokia
youtube_search_url: https://www.youtube.com/results?search_query=Collaboratively+Building+App+Manifests+at+Scale+in+Complex+Organizations+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Collaboratively Building App Manifests at Scale in Complex Organizations - Wim Henderickx, Nokia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Application + Delivery]]
- Temas: [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Wim Henderickx, Nokia
- Schedule: https://kccnceu2023.sched.com/event/1HydY/collaboratively-building-app-manifests-at-scale-in-complex-organizations-wim-henderickx-nokia
- Busca YouTube: https://www.youtube.com/results?search_query=Collaboratively+Building+App+Manifests+at+Scale+in+Complex+Organizations+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Collaboratively Building App Manifests at Scale in Complex Organizations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HydY/collaboratively-building-app-manifests-at-scale-in-complex-organizations-wim-henderickx-nokia
- YouTube search: https://www.youtube.com/results?search_query=Collaboratively+Building+App+Manifests+at+Scale+in+Complex+Organizations+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ms9gSuC8I6E
- YouTube title: Collaboratively Building App Manifests at Scale in Complex Organizations - Wim Henderickx, Nokia
- Match score: 0.953
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/collaboratively-building-app-manifests-at-scale-in-complex-organizatio/Ms9gSuC8I6E.txt
- Transcript chars: 29414
- Keywords: package, network, functions, environment, approach, cluster, deploy, important, control, nephew, configuration, function, deployed, native, change, certain, context, specialization

### Resumo baseado na transcript

uh my name is William Hendricks I was so I'm from Nokia so I was supposed to be accompanied by John but from Google but unfortunately he couldn't make it so you have to deal with me so the talk that I'm going to give the title is rather extensive right but I think there is three important aspects that I believe that are represented in the title that are important so the first one is collaboration the second is manifests and the third is scale in complex organization so

### Excerpt da transcript

uh my name is William Hendricks I was so I'm from Nokia so I was supposed to be accompanied by John but from Google but unfortunately he couldn't make it so you have to deal with me so the talk that I'm going to give the title is rather extensive right but I think there is three important aspects that I believe that are represented in the title that are important so the first one is collaboration the second is manifests and the third is scale in complex organization so I think these are the three main themes that I'm going to uh let's say talk about and try to get a representation on how we deal with this in a specific example so I because these are Concepts which are very generic right so I think it's always good to look at a specific example on how we could deal with those one thing I would say is that the example that I have is Telco because I'm from Nokia right there's also people from Ericsson here so uh what I want to say is that the example as such or what you see here as a framework that we are building it's not specific to this use case Okay so keep that in mind right so there was a talk this morning at 11 o'clock for someone who says who was talking about how to deal with large yaml manifests in an organization you see that the approach that we are taking is actually also applicable in such an environment right so keep that in mind so we'll use Telco as a use case but it's not limited to it okay now how many in the room are Telco or from the Telco space so quite a bit okay thank you so half of the room somehow there are a bunch of acronyms here which probably for the rest of the people doesn't mean anything right so when I talk about UPF or SMF and AMF think about I as an app and I'm looking at it as a network function I so that's how we call it so it's a network function it's an app and when we talk about manifests we talk about the Manifest to deploy or configure such an app right so just to give you that perspective why did I put this example here I first of all is what our main business is about but secondly there are two important things that you see here it's want to scale if you look to the numbers at the bottom right you see here on the let's say right hand side hundred thousand plus sites right so all of these things are being developed more and more in Cloud native way so that means that they are leveraging kubernetes so they will be deployed on a kubernetes environment in a cloud native uh stack and as such that gives a certain set of
