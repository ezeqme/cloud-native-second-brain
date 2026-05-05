---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "101 Track"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Ricardo Katz", "VMware", "Carlos Panato", "Chainguard"]
sched_url: https://kccncna2022.sched.com/event/182DT/why-cant-kubernetes-devs-just-add-this-new-feature-seems-so-easy-understanding-the-feature-lifecycle-in-kubernetes-ricardo-katz-vmware-carlos-panato-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=%E2%80%9CWhy+Can%E2%80%99t+Kubernetes+Devs+Just+Add+This+New+Feature%3F+Seems+So+Easy%21%E2%80%9D+-+Understanding+the+Feature+Lifecycle+In+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# “Why Can’t Kubernetes Devs Just Add This New Feature? Seems So Easy!” - Understanding the Feature Lifecycle In Kubernetes - Ricardo Katz, VMware & Carlos Panato, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[101 Track]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Ricardo Katz, VMware, Carlos Panato, Chainguard
- Schedule: https://kccncna2022.sched.com/event/182DT/why-cant-kubernetes-devs-just-add-this-new-feature-seems-so-easy-understanding-the-feature-lifecycle-in-kubernetes-ricardo-katz-vmware-carlos-panato-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=%E2%80%9CWhy+Can%E2%80%99t+Kubernetes+Devs+Just+Add+This+New+Feature%3F+Seems+So+Easy%21%E2%80%9D+-+Understanding+the+Feature+Lifecycle+In+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre “Why Can’t Kubernetes Devs Just Add This New Feature? Seems So Easy!” - Understanding the Feature Lifecycle In Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182DT/why-cant-kubernetes-devs-just-add-this-new-feature-seems-so-easy-understanding-the-feature-lifecycle-in-kubernetes-ricardo-katz-vmware-carlos-panato-chainguard
- YouTube search: https://www.youtube.com/results?search_query=%E2%80%9CWhy+Can%E2%80%99t+Kubernetes+Devs+Just+Add+This+New+Feature%3F+Seems+So+Easy%21%E2%80%9D+-+Understanding+the+Feature+Lifecycle+In+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pEYpvYVlgQc
- YouTube title: “Why Can’t Kubernetes Devs Just Add This New Feature? Seems So Easy!” - Ricardo Katz & Carlos Panato
- Match score: 0.782
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/why-cant-kubernetes-devs-just-add-this-new-feature-seems-so-easy-under/pEYpvYVlgQc.txt
- Transcript chars: 28807
- Keywords: feature, network, actually, discussions, sometimes, discuss, process, security, implement, better, someone, change, discussion, discussing, features, policy, product, breaking

### Resumo baseado na transcript

okay uh welcome everybody uh thanks for attending this talk [Music] my name is Carlos panatu I work at chain guard and I also I'm Tech lead on the Sig release and kubernetes and I maintain other projects in the cloud Community as well hey welcome everyone my name is Ricardo I work for VMware I am one of the Ingress in Gen X maintainers as well and you can find me around in ccla sometimes and yeah you can find me around messing with code breaking breaking things with an enhancement does this need like a blog post does it require more sigs is this just something for Network or like network security and maybe the API or whatever does it redesign something it's a big effort in part impact user experience and so

### Excerpt da transcript

okay uh welcome everybody uh thanks for attending this talk [Music] my name is Carlos panatu I work at chain guard and I also I'm Tech lead on the Sig release and kubernetes and I maintain other projects in the cloud Community as well hey welcome everyone my name is Ricardo I work for VMware I am one of the Ingress in Gen X maintainers as well and you can find me around in ccla sometimes and yeah you can find me around messing with code breaking breaking things with today's talk we're gonna like try to understand like the future life cycle in kubernetes and how we like people can open features and like do implementing to the whole life cycle uh before we start like uh we have three questions the first one is who here uh is here for the first time that doesn't know anything about the caps and the future life cycle can just for curiosity okay and uh who are here that have features ideas that want to know how to push those to the through their life cycle okay okay and the final one who here open already like one or more features ideas and it's stuck in between it's like okay because think that we are jerks yeah okay thank you everybody the we're gonna go like go over some examples and then we're gonna like explain the the how the cap works in the real life for example this is the one feature idea that is like a kind of let's say easier way to roll out config Maps the future ideas like a red open till like a 2016 and uh like there is no conclusions or things yet like this feature is still open and it's not yet implemented like for example we have like a more than a thousand people like saying Jesus is a good think to have but there is no concrete like outcome from this idea here another one is like a simple startup in ordering like I still open like from like eight the 2018 there is a lot of questions and a lot of like comments and people like should we use a Readiness gate like some other new filtering field like to give ideas there's a lot of discussions a lot of closet issues around these ideas here another one that we like it's a dual stack for IPv6 was up in and it was closed like uh last year that took like uh yeah just three years to get like the full thing the full story like uh roll out and everybody agreed on those things sometimes takes less sometimes sometimes takes more time sometimes like never end right for example Ricardo opened one idea like for the printing HTTP life liveness check and this idea didn't like went through and they just closed t
