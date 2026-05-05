---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Maciej Szulik", "Defense Unicorns", "Janet Kuo", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2EF4v/sig-apps-updates-building-the-next-generation-of-kubernetes-workloads-together-maciej-szulik-defense-unicorns-janet-kuo-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Apps+Updates%3A+Building+the+Next+Generation+of+Kubernetes+Workloads+Together+CNCF+KubeCon+2026
slides: []
status: parsed
---

# SIG Apps Updates: Building the Next Generation of Kubernetes Workloads Together - Maciej Szulik, Defense Unicorns & Janet Kuo, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Maciej Szulik, Defense Unicorns, Janet Kuo, Google
- Schedule: https://kccnceu2026.sched.com/event/2EF4v/sig-apps-updates-building-the-next-generation-of-kubernetes-workloads-together-maciej-szulik-defense-unicorns-janet-kuo-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Apps+Updates%3A+Building+the+Next+Generation+of+Kubernetes+Workloads+Together+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre SIG Apps Updates: Building the Next Generation of Kubernetes Workloads Together.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4v/sig-apps-updates-building-the-next-generation-of-kubernetes-workloads-together-maciej-szulik-defense-unicorns-janet-kuo-google
- YouTube search: https://www.youtube.com/results?search_query=SIG+Apps+Updates%3A+Building+the+Next+Generation+of+Kubernetes+Workloads+Together+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uj2WVzDndt4
- YouTube title: SIG Apps Updates: Building the Next Generation of Kubernetes Workloads... Maciej Szulik & Janet Kuo
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sig-apps-updates-building-the-next-generation-of-kubernetes-workloads/uj2WVzDndt4.txt
- Transcript chars: 22728
- Keywords: stateful, basically, sandbox, working, controller, talking, within, running, started, particular, deployment, default, actually, whether, certain, modify, resources, create

### Resumo baseado na transcript

We are going to talk about building the next generation of Kubernetes workloads together. We focus on the application use case and then we own the core workflow APIs including the deployment stful set jobs and chrome jobs and demon set etc. Our hope is that if that uh that the work that we're currently um ongoing, we will be able to address all the po possible problems and and then within like 137 and 138 we'll be able to move this forward. uh because it was actually uh some person showing up on our slack like listen this is the problem that I were seeing in a max and available in a stateful set and we started going back and forth they only after only after they described us what the problem is how they approached it we were able to nail down where uh where the problem is how to fix it and then eventually uh move forward with it so uh big shout out also to the people I can't remember their name uh but they they do reach out to us and we were able thanks to their uh feedback address the problems.

### Excerpt da transcript

Hi everyone, welcome to the SAPS talk. We are going to talk about building the next generation of Kubernetes workloads together. So what is SIG apps? We focus on the application use case and then we own the core workflow APIs including the deployment stful set jobs and chrome jobs and demon set etc. And we also develop the application level tools and standards. And we are also exploring more uh Kubernetes native standards for AI given that AI is so popular now. And then before I move on, let's introduce ourselves. I'm Janet. I'm from Google. I'm one of the lead of SAPS. >> Uh my name is Mache. I'm also co-leading um SIG apps with Janet. Sadly, Kennet is the third uh person in charge that you should be chasing if you want to get stuff added within the our preview. Uh Canon couldn't be with us. Um but yeah, that's the the three of us. >> So, we have a few new beta features in 135. There's a maximum available for staple sets. It's for faster and more flexible row out. It improves the roll out speed. It was enabled by default before, but because we discovered some edge cases that's not covered in the feature yet.

So, this is disabled by feature uh disabled by default for now. And then huge shout out to HA. >> Yeah. who helped implement this feature. >> Yeah. And disablement is like a fresh thing because we found a problem literally like a week prior to CubeCon. We started look looking into it. Thanks to Philillip for noticing that there were some additional edge cases and after discussion back and forth about the direction we decided that um we know that there is a problem and we want to make sure that all the edge cases are covered. There are some significant uh problems that we will have to figure out. We will be rolling back uh 136 will have it disabled off. The next uh point uh point version of 135 will also have it disabled. So if you are relying on those features being on, you'll have to make sure that the feature gate behind it will be uh will need to be enabled. Our hope is that if that uh that the work that we're currently um ongoing, we will be able to address all the po possible problems and and then within like 137 and 138 we'll be able to move this forward.

Uh but that also shows how important for us is the feedback that we're getting from you the users. uh because it was actually uh some person showing up on our slack like listen this is the problem that I were seeing in a max and available in a stateful set and we started going back and forth
