---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Keynote Sessions"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Vaibhav Kamra", "Chief Technology Officer", "Kasten by Veeam"]
sched_url: https://kccnceu2021.sched.com/event/ijBI/sponsored-keynote-day-2-with-kubernetes-this-is-fine-vaibhav-kamra-chief-technology-officer-kasten-by-veeam
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Day+2+with+Kubernetes+-+This+Is+Fine%21+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Keynote: Day 2 with Kubernetes - This Is Fine! - Vaibhav Kamra, Chief Technology Officer, Kasten by Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Vaibhav Kamra, Chief Technology Officer, Kasten by Veeam
- Schedule: https://kccnceu2021.sched.com/event/ijBI/sponsored-keynote-day-2-with-kubernetes-this-is-fine-vaibhav-kamra-chief-technology-officer-kasten-by-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Day+2+with+Kubernetes+-+This+Is+Fine%21+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Day 2 with Kubernetes - This Is Fine!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/ijBI/sponsored-keynote-day-2-with-kubernetes-this-is-fine-vaibhav-kamra-chief-technology-officer-kasten-by-veeam
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Day+2+with+Kubernetes+-+This+Is+Fine%21+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=znr1YXhAZss
- YouTube title: Sponsored Keynote: Day 2 with Kubernetes - This Is Fine! - Vaibhav Kamra, Chief Technology Officer
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-keynote-day-2-with-kubernetes-this-is-fine/znr1YXhAZss.txt
- Transcript chars: 5124
- Keywords: access, environments, business, ransomware, platform, number, having, automation, applications, experiences, clusters, challenges, production, misconfigured, impact, planning, everyone, kubecon

### Resumo baseado na transcript

[Music] hello everyone it's great to be here at kubecon eu my name is web of camara and i'm the cto here at cast and by veeam at castin we focus on data protection so backup and recovery for kubernetes applications uh this is my sixth year here at kubecon it's really an amazing event i love coming here because it's a great way to learn what the community has been doing as well as share experiences with with everybody out there in the same journey so in that spirit

### Excerpt da transcript

[Music] hello everyone it's great to be here at kubecon eu my name is web of camara and i'm the cto here at cast and by veeam at castin we focus on data protection so backup and recovery for kubernetes applications uh this is my sixth year here at kubecon it's really an amazing event i love coming here because it's a great way to learn what the community has been doing as well as share experiences with with everybody out there in the same journey so in that spirit what i'd like to do today is talk a little bit about our experiences with our kubernetes platform development as well as what we've observed working with a large number of customers as they've scaled out the number of users the number of clusters the number of applications they have and really the challenges they ran into this is very much a here and now problem if we look at the most recent cncf survey 80 of us who took the survey indicated that we are uh running kubernetes in production and what we're also seeing is that the journey from pilot to production it's going much faster just because of the maturity of the tooling that's out there as well as all the learnings and education that's available to us now security and business continuity are two key challenges that i wanted to focus on how do we keep make sure our environments are secure both from internal and external threats from breaches if vulnerabilities show up how are we going to address them soon and fast how are we going to detect those things how are we going to deal with ransomware so these are some of the key what we call day two challenges things that show up after you've gone through the initial stage of of platform development a lot of issues that we observe actually come down to misconfigured access that is our users or tenants have too much access to the platform there is this desire to enable self-service in these environments to allow our users to be able to do what they need to do without having to involve operations or file a ticket for everything but what that can lead to is misconfigured policies privilege escalation is also very common it's not just direct access to api resources that you have to worry about sometimes but what access to other operators do users have in this environment do these operators that often have privileged access to the cluster do they expose apis that allow you to control who can access it or who cannot because if not then users this can be privileged escalation just because a user has access
