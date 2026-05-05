---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Service Mesh"
themes: ["Security", "Networking", "SRE Reliability"]
speakers: ["Christopher Voss", "Microsoft"]
sched_url: https://kccnceu2022.sched.com/event/ytuJ/service-mesh-at-scale-how-xbox-cloud-gaming-secures-22k-pods-with-linkerd-christopher-voss-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Service+Mesh+at+Scale%3A+How+Xbox+Cloud+Gaming+Secures+22k+Pods+with+Linkerd+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Service Mesh at Scale: How Xbox Cloud Gaming Secures 22k Pods with Linkerd - Christopher Voss, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Service Mesh]]
- Temas: [[Security]], [[Networking]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Christopher Voss, Microsoft
- Schedule: https://kccnceu2022.sched.com/event/ytuJ/service-mesh-at-scale-how-xbox-cloud-gaming-secures-22k-pods-with-linkerd-christopher-voss-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Service+Mesh+at+Scale%3A+How+Xbox+Cloud+Gaming+Secures+22k+Pods+with+Linkerd+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Service Mesh at Scale: How Xbox Cloud Gaming Secures 22k Pods with Linkerd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytuJ/service-mesh-at-scale-how-xbox-cloud-gaming-secures-22k-pods-with-linkerd-christopher-voss-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Service+Mesh+at+Scale%3A+How+Xbox+Cloud+Gaming+Secures+22k+Pods+with+Linkerd+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Mh0Wqu3v8h0
- YouTube title: Service Mesh at Scale: How Xbox Cloud Gaming Secures 22k Pods with Linkerd - Christopher Voss
- Match score: 0.976
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/service-mesh-at-scale-how-xbox-cloud-gaming-secures-22k-pods-with-link/Mh0Wqu3v8h0.txt
- Transcript chars: 18993
- Keywords: canary, mesh, little, deployments, linker, metrics, wanted, inside, essentially, clusters, obviously, prometheus, important, several, around, gaming, cluster, meshes

### Resumo baseado na transcript

i'm chris voss that's a picture of me if you can't see me from the back um i'm a senior software development engineer at microsoft i joined both microsoft and xbox cloud gaming in 2018 august or so originally i was uh on the team that is managing our xbox servers um keeping them healthy making sure they're up to date all that fun stuff um more recently last couple years i've been on our infrastructure team um game game streaming shared services our team manages and operates the infrastructure

### Excerpt da transcript

i'm chris voss that's a picture of me if you can't see me from the back um i'm a senior software development engineer at microsoft i joined both microsoft and xbox cloud gaming in 2018 august or so originally i was uh on the team that is managing our xbox servers um keeping them healthy making sure they're up to date all that fun stuff um more recently last couple years i've been on our infrastructure team um game game streaming shared services our team manages and operates the infrastructure for xbox cloud gaming services so you know azure resources such as cosmos db or storage accounts or key vaults all that fun stuff our kubernetes clusters obviously and then we also have some services that are kind of shared across all of our other teams that we also own if you'd like to contact me these certainly work i'm sure there are others that i forgot but you know if you want to reach out to me these are definitely good places so a little bit about xbox cloud gaming so um it comes for free if you have xbox game pass ultimate and basically it enables you to play games wherever you want on whatever device you want and our motto is or our mission rather is allowing people to play the games you want with the people you want on the devices you already own you know it's important uh to us um you know to enable anyone who would like to play games to play those games it's you know it's a way of connecting people who might be you know from great distances and giving them shared experiences and um so yeah that's a big motivation behind our team and our product um so a little bit about what our footprint looks like we have roughly aks clusters and aks is azure kubernetes services i forgot to add that in there but across several azure regions we have 50 or so micro services i think it's a little bit more than that now but 50 plus is good and about 700 to 1000 pods per cluster so yeah spread spread across those 26-ish clusters um we have about 22 000 pods around the world um and and just a little bit about the servers you know so when you're playing a game um you're streaming a game um what you're streaming from is actually a xbox series x hardware um it's a custom design modification of the xbox series x hardware and it's deployed in data centers around the globe so when you're playing you're really playing on an xbox and then we're giving you all the signals um and uh allowing and then allowing your feedback to come back and connect to that console so a little bit about ou
