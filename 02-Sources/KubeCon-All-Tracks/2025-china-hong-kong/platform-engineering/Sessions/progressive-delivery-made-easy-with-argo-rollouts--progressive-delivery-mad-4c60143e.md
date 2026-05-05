---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Platform Engineering"
themes: ["Platform Engineering", "GitOps Delivery"]
speakers: ["Kevin Dubois", "Red Hat"]
sched_url: https://kccncchn2025.sched.com/event/1x5jk/progressive-delivery-made-easy-with-argo-rollouts-kevin-dubois-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Progressive+Delivery+Made+Easy+With+Argo+Rollouts+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Progressive Delivery Made Easy With Argo Rollouts - Kevin Dubois, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]]
- País/cidade: China / Hong Kong
- Speakers: Kevin Dubois, Red Hat
- Schedule: https://kccncchn2025.sched.com/event/1x5jk/progressive-delivery-made-easy-with-argo-rollouts-kevin-dubois-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Progressive+Delivery+Made+Easy+With+Argo+Rollouts+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Progressive Delivery Made Easy With Argo Rollouts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5jk/progressive-delivery-made-easy-with-argo-rollouts-kevin-dubois-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Progressive+Delivery+Made+Easy+With+Argo+Rollouts+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=C34TJFDsq-s
- YouTube title: Progressive Delivery Made Easy With Argo Rollouts - Kevin Dubois, Red Hat
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/progressive-delivery-made-easy-with-argo-rollouts/C34TJFDsq-s.txt
- Transcript chars: 27937
- Keywords: production, version, traffic, little, release, argo, everything, delivery, canary, rollouts, deploy, continuous, testing, deployment, gitops, environment, automatically, progressive

### Resumo baseado na transcript

Uh in this session we're going to talk about progressive delivery um with the Argo rollouts which is part of the Argo project. also uh part of the developer experience uh tag uh and I'm from Belgium so far away long flight um all right so this is kind of uh how it started for me um a long time ago and I'm not sure if it was Um but you know over the years too we went from more monolithic architectures to more distributed architectures and then you know you you know the the kind of the promise of microservices where you have multiple teams working on multiple projects which is great. you define all that in the Kubernetes world probably in in uh in the form of YAML you commit those to a git repository and so you can treat everything as code not just your uh your actual code but also everything that goes around Uh it's a declarative uh GitOps continuous delivery tool for Kubernetes uh which allows you to do exactly that, right? And then you can use metrics to kind of see is everything going well in my production environment on a subset of of this uh deployment uh to then determine whether you want to release further or not.

### Excerpt da transcript

Good afternoon. Uh in this session we're going to talk about progressive delivery um with the Argo rollouts which is part of the Argo project. Um so quick introduction about myself. I'm Kevin Dubois. I'm a developer advocate at uh at Red Hat. Uh I'm also a Java champion. also uh part of the developer experience uh tag uh and I'm from Belgium so far away long flight um all right so this is kind of uh how it started for me um a long time ago and I'm not sure if it was FileZilla I think it was another tool that was before but in any case you know that's how we uh delivered our software back in the day is copy and you know kind of drag and dropping files or maybe it was in the CLI. I don't quite remember, but it was definitely FTP. Um, and uh, yeah, we had quite a few production outages back back then because uh, yeah, it was hard to kind of uh, test something before it went to production. Not so great, right? And this was uh, even before uh, git. So, we didn't even have version control or anything. So, then, you know, we started using uh, git.

Um well first it was subversion and uh maybe some other tool but eventually we we went to git and that was already great because at least you know now we could uh do a revert and then copy and paste things back and forth and then uh we started using r sync and you know we we'd uh write some crazy Python scripts to automate stuff and um still overnight we had outages and I remember many nights uh being up to deploy Then uh we you know kind of evolved and started using CI/CD and you know you probably all have uh have maybe worked with Jenkins in the past or maybe even today and uh you know so basically with CI/CD what you do is you know you go through this kind of uh phase of build test uh maybe ideally do some security checks to uh create a release and then deploy maybe to staging environment and then deploy to production. So you have this kind of continuous integration where you uh build your projects and you make sure somebody commits and then uh that gets integrated into the project and then uh continuous delivery kind of uh to get it to production.

Continuous delivery typically kind of has this uh manual process of making sure that yes we're ready to go to production and then uh we'll uh we'll actually deploy. Um but you know over the years too we went from more monolithic architectures to more distributed architectures and then you know you you know the the kind of the promise of microservices where you have multi
