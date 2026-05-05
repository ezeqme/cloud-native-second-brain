---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Security", "Kubernetes Core"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQk7/want-to-secure-k8s-clusters-think-paralus-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Want+to+secure+K8s+clusters%3F+Think+Paralus.+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Want to secure K8s clusters? Think Paralus. | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQk7/want-to-secure-k8s-clusters-think-paralus-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Want+to+secure+K8s+clusters%3F+Think+Paralus.+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Want to secure K8s clusters? Think Paralus. | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQk7/want-to-secure-k8s-clusters-think-paralus-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Want+to+secure+K8s+clusters%3F+Think+Paralus.+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7_NqnnBqLls
- YouTube title: Want to secure K8s clusters? Think Paralus. | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/want-to-secure-k8s-clusters-think-paralus-project-lightning-talk/7_NqnnBqLls.txt
- Transcript chars: 7503
- Keywords: access, permissions, cluster, clusters, parallel, paralles, couple, paralus, whenever, management, happens, issues, github, parallels, paralis, resources, manage, around

### Resumo baseado na transcript

hi and good evening everyone uh I am Atul and I'm going to be talking about Paralis which is a cncf Sandbox project uh and the whole idea of building Paralis was to enable zero trust access for kubernetes resources uh I'm sure when whenever we are dealing with kubernetes we know that access management is a critical thing and often gets complex uh what what happens is that while it provides rback out of the box uh especially when you are scaling and you know when you have a

### Excerpt da transcript

hi and good evening everyone uh I am Atul and I'm going to be talking about Paralis which is a cncf Sandbox project uh and the whole idea of building Paralis was to enable zero trust access for kubernetes resources uh I'm sure when whenever we are dealing with kubernetes we know that access management is a critical thing and often gets complex uh what what happens is that while it provides rback out of the box uh especially when you are scaling and you know when you have a lot of users lot of resources that come into play it becomes really difficult to manage all the permissions uh because you know you can lead into issues like uh you know uh free permissions roaming around so you know for example you had a team and people move you know there's a churn in the team then you know it becomes difficult to manage those permissions and track those permission and who has what access and I think that's where uh zero trust as a principle comes in uh very handy and paralus is one project that gives you RB back but with zero trust built uh zero trust access built in so one of the things that parales does great is uh just in time access management so by tradition what happens in kubernetes is you know you define roles you define permissions you define uh you know users and then you assign these things to them but one of the things that parallel gives you out of the box is uh just in time access management plus it also allows you to mix and match your roles and permissions that you need so you know you can create your own role you can you can mix and match permissions uh you know whatever you you need uh you need to provide we have a certain set of permissions that are provided uh by default and then after that you know you can add your own uh you know permissions that you want and assign it to the roles that you need uh also since this is just in time you know by default zero trust is embedded in it so by default if anyone tries to access obviously they don't have access to it so it it all happens just in time uh outside of that what it also does is it enables you to use your existing SSO So currently it has support for GitHub gitlab Google uh and Microsoft I guess but apart from that if you have any other SSO third party SSO that you're using something like a key clo you can easily integrate parallel with it so it will keep everything whatever you have existing uh and you can just bring in uh any other SSO that you that you want uh and then you can manage resources f
