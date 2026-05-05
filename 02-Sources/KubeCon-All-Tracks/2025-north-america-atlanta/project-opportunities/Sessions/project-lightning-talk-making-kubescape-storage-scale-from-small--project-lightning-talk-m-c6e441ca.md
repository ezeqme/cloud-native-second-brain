---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "GitOps Delivery", "SRE Reliability", "Community Governance"]
speakers: ["Ben Hirschberg", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d5d/project-lightning-talk-making-kubescape-storage-scale-from-small-and-mid-size-to-huge-deployments-ben-hirschberg-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Making+Kubescape+Storage+Scale+From+Small+and+Mid-Size+To+Huge+Deployments+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Making Kubescape Storage Scale From Small and Mid-Size To Huge Deployments - Ben Hirschberg, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[GitOps Delivery]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Ben Hirschberg, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d5d/project-lightning-talk-making-kubescape-storage-scale-from-small-and-mid-size-to-huge-deployments-ben-hirschberg-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Making+Kubescape+Storage+Scale+From+Small+and+Mid-Size+To+Huge+Deployments+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Making Kubescape Storage Scale From Small and Mid-Size To Huge Deployments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5d/project-lightning-talk-making-kubescape-storage-scale-from-small-and-mid-size-to-huge-deployments-ben-hirschberg-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Making+Kubescape+Storage+Scale+From+Small+and+Mid-Size+To+Huge+Deployments+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0SxXulvdMMs
- YouTube title: Project Lightning Talk: Making Kubescape Storage Scale From Small and Mid-Size To... Ben Hirschberg
- Match score: 0.955
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-making-kubescape-storage-scale-from-small-and-m/0SxXulvdMMs.txt
- Transcript chars: 7555
- Keywords: objects, object, server, application, patching, support, deployments, cubscape, cubecape, security, producing, profiles, custom, within, listing, changing, started, metadata

### Resumo baseado na transcript

Thank you for staying for I think the last one of the last uh lightning talks. So I'm Ben uh CTO and co-founder of the company Armo and also one of the maintainers of the Cubscape CNCF project. Uh um so tapping into this super nice Kubernetes API ecosystem like using cubectl to get objects to the K9S lens headlamp like all these things and it's like super sleek it's super duper but the problem was when we needed to start to scale So, one of the you know options in Kubernetes API uh uh is to uh uh you know to store Kubernetes objects and then list them. But the problem was for us that it's it's really really hard again because of big objects because of you know maybe it's not really needed in the security world to watch things like you don't necessarily need to get these live updates of vulnerability scans maybe or for even uh I don't know application profiles uh and it made us a tremendous effort in our storage component to just back this prom kubernetes promise up so it it was like super duper card.

### Excerpt da transcript

Thank you for staying for I think the last one of the last uh lightning talks. So I'm Ben uh CTO and co-founder of the company Armo and also one of the maintainers of the Cubscape CNCF project. Now uh if you do you like memes? Do you like memes? >> Yeah. Okay. Do you like project maintainers whining? >> Yeah. Okay. So this talk is for you. Um, so I'm going to lose a use a lot of memes. Actually, this is like the only uh uh slide without meme. Um, so just a few words about CubeCape. Cubscape is a CNCF project in incubation. Uh, Cubscape is a security platform for Kubernetes. Uh, we are doing a lot of scanning and producing data stuff. We are scanning for vulnerabilities, configuration issues. We are generating network policies, SECOM profiles. We are doing runtime thread detection and and we are doing application profiling and creating these application uh object called application profiles. What it does is actually produces a lot of data. So we were thinking we're thinking okay what how what would we do with this allow tons of data that we are producing for the users how can they tap into this data and we're really contemplating about okay whether we are like just creating this intern uh you know cubecape API server where you can just like build bring these objects and read them and like uh use them as you want or you will publish them as Kubernetes API objects.

Do we like Kubernetes API objects? Of course we do. They are lovely. Like okay now the next questions is okay where do we store them? So do we use define them as CRDs Kubernetes custom resources and let just at CD store them or do we use an aggregated API server with the Kubernetes API? So is there anyone who knows what an aggregated API server is? Hands up. Okay. So you guess but you don't count. Uh uh uh uh so uh um so the point is that you can create your own API server within the Kubernetes cluster and the Kubernetes API server will just like forward all the requests to your API server. So you can still you know be suple like tapping into whoa no memes for you. Uh um so tapping into this super nice Kubernetes API ecosystem like using cubectl to get objects to the K9S lens headlamp like all these things and it's like super sleek it's super duper but the problem was when we needed to start to scale this information with huge cluster deployments and you see the sweat like it's we were sweating and in this talk I'm going to show you like a few things that made us like made our lives hell and how w
