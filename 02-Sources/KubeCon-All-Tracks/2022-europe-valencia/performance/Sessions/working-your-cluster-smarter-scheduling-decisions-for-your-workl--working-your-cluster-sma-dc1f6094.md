---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Madalina Lazar", "Denisio Togashi", "Intel"]
sched_url: https://kccnceu2022.sched.com/event/ytlh/working-your-cluster-smarter-scheduling-decisions-for-your-workloads-madalina-lazar-denisio-togashi-intel
youtube_search_url: https://www.youtube.com/results?search_query=Working+your+Cluster%3A+Smarter+Scheduling+Decisions+for+Your+Workloads+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Working your Cluster: Smarter Scheduling Decisions for Your Workloads - Madalina Lazar & Denisio Togashi, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Madalina Lazar, Denisio Togashi, Intel
- Schedule: https://kccnceu2022.sched.com/event/ytlh/working-your-cluster-smarter-scheduling-decisions-for-your-workloads-madalina-lazar-denisio-togashi-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Working+your+Cluster%3A+Smarter+Scheduling+Decisions+for+Your+Workloads+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Working your Cluster: Smarter Scheduling Decisions for Your Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlh/working-your-cluster-smarter-scheduling-decisions-for-your-workloads-madalina-lazar-denisio-togashi-intel
- YouTube search: https://www.youtube.com/results?search_query=Working+your+Cluster%3A+Smarter+Scheduling+Decisions+for+Your+Workloads+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=csg7ZQXQ5u8
- YouTube title: Working your Cluster: Smarter Scheduling Decisions for Your Work... Madalina Lazar & Denisio Togashi
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/working-your-cluster-smarter-scheduling-decisions-for-your-workloads/csg7ZQXQ5u8.txt
- Transcript chars: 25413
- Keywords: scheduling, schedule, scheduler, metrics, strategy, policy, metric, actually, default, related, cluster, gpu, deployment, method, available, question, working, workload

### Resumo baseado na transcript

hi everyone thank you very much for joining us today uh especially in person i know it's been uh somewhere like the weird the last years have been a bit weird so at least from my point not sure if you can relate this this is like i haven't seen this many people in like the last two or three years so it's a bit different uh so thank you very much for being here thank you very much for the people that are uh virtually attending um [Music] my

### Excerpt da transcript

hi everyone thank you very much for joining us today uh especially in person i know it's been uh somewhere like the weird the last years have been a bit weird so at least from my point not sure if you can relate this this is like i haven't seen this many people in like the last two or three years so it's a bit different uh so thank you very much for being here thank you very much for the people that are uh virtually attending um [Music] my name is madalina i'll be one of your co-hosts today i am a software engineer in intel's resource management space in ireland i have a web service and distributed systems background but i recently moved into the cloud native and kubernetes space i won't be giving this presentation alone i'm here with my teammate denisio and he's going to say a couple of words about himself hello my name is denis otogashes or ice mandolin i am also a cloud native engineer at intel my background is science then a couple years ago um i got uh opportunities to fast track and get a degree on the soft development and and then so i end up on this huge incred incredible company that intel so we both are based in ireland we work on the team on the resource management team and in this team um we have so many different projects but each one then with your challenge it's your the challenges and so on but um we we always looking on different ways to make an improvement kind of different innovations related but with the mindset what was talked on this morning uh relate to sustainability so as i said we we have a dual school projects and uh yeah i hope you enjoy so madeline and i is a first time um community uh cubicon so um it's really great to be here and yeah um today because of you and thank you give you this opportunity we're going to talk about one of those projects that is related on the um you know this math scheduling and and then we follow up the presentation that so i stopped to talk and head back to mata thank you so i um so the name of our talk is working your cluster smarter scheduling decisions for your workload the aim of it is to show you how you can leverage telemetry from your own cluster to make better scheduling decisions we're going to start off with why resource dates and scheduling matter how would they how would you go around combining them and what's the what are the benefits of doing so we're going to touch on one of our projects which is called telemetry aware scheduling it's an open source project then you spoke a bit about
