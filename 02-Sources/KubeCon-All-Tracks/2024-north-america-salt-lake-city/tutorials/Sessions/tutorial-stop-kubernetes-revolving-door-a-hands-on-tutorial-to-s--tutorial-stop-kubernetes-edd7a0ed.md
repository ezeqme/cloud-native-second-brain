---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Tutorials"
themes: ["Security", "Kubernetes Core"]
speakers: ["Savitha Raghunathan", "Rey Lejano", "Red Hat", "Mahé Tardy", "Isovalent at Cisco"]
sched_url: https://kccncna2024.sched.com/event/1i7rJ/tutorial-stop-kubernetes-revolving-door-a-hands-on-tutorial-to-secure-a-kubernetes-cluster-savitha-raghunathan-rey-lejano-red-hat-mahe-tardy-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Stop+Kubernetes%27+Revolving+Door%3A+A+Hands-on+Tutorial+to+Secure+a+Kubernetes+Cluster+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: Stop Kubernetes' Revolving Door: A Hands-on Tutorial to Secure a Kubernetes Cluster - Savitha Raghunathan & Rey Lejano, Red Hat; Mahé Tardy, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Savitha Raghunathan, Rey Lejano, Red Hat, Mahé Tardy, Isovalent at Cisco
- Schedule: https://kccncna2024.sched.com/event/1i7rJ/tutorial-stop-kubernetes-revolving-door-a-hands-on-tutorial-to-secure-a-kubernetes-cluster-savitha-raghunathan-rey-lejano-red-hat-mahe-tardy-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Stop+Kubernetes%27+Revolving+Door%3A+A+Hands-on+Tutorial+to+Secure+a+Kubernetes+Cluster+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: Stop Kubernetes' Revolving Door: A Hands-on Tutorial to Secure a Kubernetes Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rJ/tutorial-stop-kubernetes-revolving-door-a-hands-on-tutorial-to-secure-a-kubernetes-cluster-savitha-raghunathan-rey-lejano-red-hat-mahe-tardy-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Stop+Kubernetes%27+Revolving+Door%3A+A+Hands-on+Tutorial+to+Secure+a+Kubernetes+Cluster+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pfzlJaZdNCg
- YouTube title: Tutorial: Stop Kubernetes' Revolving Door: A Hands-on Tutoria... S. Raghunathan, R. Lejano, M. Tardy
- Match score: 0.773
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-stop-kubernetes-revolving-door-a-hands-on-tutorial-to-secure/pfzlJaZdNCg.txt
- Transcript chars: 62820
- Keywords: cluster, actually, create, namespace, security, control, running, bindings, default, binding, created, controller, target, access, accounts, masters, network, policies

### Resumo baseado na transcript

welcome everyone thank you for joining for this Friday afternoon session uh today we are going to have stop kubernetes revolving doors and some tutorial to secure a cuetes cluster so my name is May I'm working as a software engineer at isov villance uh let me introduce Savita thank you thank you mah My name is Savita ragunan I am a senior software engineer at redart I also work with Mah and Reay on the SEC kuity Sig Security Group I'm the lead for six security documentations of project kubernetes doio with one equal Baseline it's labed and now if we want to create a pod that actually uh um violate that Baseline policy so this one will just try to create a privilege pod um what will happen is that the pod should be created but like the user will receive a warning um like that this pod will violate like the post security basine latest uh because of like the security cons. p with exactly the same security context with privilege equal true what happens is that it gets rejected so this is like the same thing as before but then like any violation actually rejects the action so you can see it's forbidden and if we in your control plane node uh in a kind cluster and in many other distributions of kubernetes you may not have access to that yaml file uh so we need to explore uh through the CBE controller manager pod so this lab or this module

### Excerpt da transcript

welcome everyone thank you for joining for this Friday afternoon session uh today we are going to have stop kubernetes revolving doors and some tutorial to secure a cuetes cluster so my name is May I'm working as a software engineer at isov villance uh let me introduce Savita thank you thank you mah My name is Savita ragunan I am a senior software engineer at redart I also work with Mah and Reay on the SEC kuity Sig Security Group I'm the lead for six security documentations of project and now I'll pass it over to Ray hey folks my name is Ray Lano I'm a Solutions architect at Red ha hats I'm also uh one of the co-chairs of kubernetes Sig docs I'm also one of the sub project leads for Sig security so I help run the external security audit of for the project and if you don't know um Upstream kubernetes by default is not secure guard rails are not in place when you install Upstream kubernetes so that means pods can freely talk to other pods even on other nodes uh if we could easily Traverse across namespaces as well uh if a user has somehow breached a pod or container they can also be able to access the the cube API server and also the the worker node itself so here we're talk we're here to talk about how to secure kubernetes and we did publish an upstream security guide checklist on how to do that thanks Ray uh yeah the security check list was merged almost two years ago now you can see in this picture that many people actually participated in its creation you have a bunch of reviewers a bunch of authors on the on the pr and we had a lot of discussion around this like uh we created some draft and then we had like something like 200 uh conversation on this uh PR so the idea the goal was to provide the Community with like a basic but solid official checklist uh that is not maybe sufficient but it's it's a nice start for starting your security Journey with kubernetes and because quite often um so it looks like that uh quite often the question about Security in kubernetes is like where to start so this checklist give you a bunch of list of pain points and how to De deep into like this uh pain point and and learn more details directly in the kubernetes documentation right once again there's a link to this kuet security checklist uh like myad said it is uh a basic security guidance uh it may not and is not sufficient for production but it is a good starting point uh so some of the sections of that security checklist is authentication and authorization uh we're goi
