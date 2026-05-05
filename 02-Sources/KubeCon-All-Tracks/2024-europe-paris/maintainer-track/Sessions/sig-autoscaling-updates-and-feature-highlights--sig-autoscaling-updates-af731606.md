---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Jonathan Innis", "AWS", "Maciek Pytel", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1Yhi2/sig-autoscaling-updates-and-feature-highlights-jonathan-innis-aws-maciek-pytel-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Autoscaling+Updates+and+Feature+Highlights+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SIG Autoscaling Updates and Feature Highlights - Jonathan Innis, AWS & Maciek Pytel, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Jonathan Innis, AWS, Maciek Pytel, Google
- Schedule: https://kccnceu2024.sched.com/event/1Yhi2/sig-autoscaling-updates-and-feature-highlights-jonathan-innis-aws-maciek-pytel-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Autoscaling+Updates+and+Feature+Highlights+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SIG Autoscaling Updates and Feature Highlights.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhi2/sig-autoscaling-updates-and-feature-highlights-jonathan-innis-aws-maciek-pytel-google
- YouTube search: https://www.youtube.com/results?search_query=SIG+Autoscaling+Updates+and+Feature+Highlights+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XWPbWM12r8g
- YouTube title: SIG Autoscaling Updates and Feature Highlights
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sig-autoscaling-updates-and-feature-highlights/XWPbWM12r8g.txt
- Transcript chars: 25947
- Keywords: cluster, expander, scaling, scaler, autoscaler, actually, multiple, recommender, change, write, running, options, recommendations, workloads, pretty, disruption, little, object

### Resumo baseado na transcript

this is the sig auto scaling update and we're going to tell you about a lot of exciting things that we've been doing since the last time we all got together take my mask off okay um why don't i guess we'll go through some introductions to begin with my name is michael mccune i work for red hat i'm an engineer we're all engineers who work in the sig auto scaling community this is uh joachim bartosik from google guy templeton from sky scanner and david morrison from airbnb

### Excerpt da transcript

this is the sig auto scaling update and we're going to tell you about a lot of exciting things that we've been doing since the last time we all got together take my mask off okay um why don't i guess we'll go through some introductions to begin with my name is michael mccune i work for red hat i'm an engineer we're all engineers who work in the sig auto scaling community this is uh joachim bartosik from google guy templeton from sky scanner and david morrison from airbnb and so when when and if we can get the slides going we're going to talk to you about some changes that have been happening on the horizontal pod auto scaler we've got an update about what's going on with the v2 api that's been released and kind of the deprecation notices around v2 beta 1 and v2 beta2 david's going to talk a little bit about the grpc editions that have come into the cluster auto scaler recently and in specific about the grpc expander that's been written and we also have some more grpc kind of provider coming as well i mean it's already there but you know and then joaquim's going to talk about the changes that have been happening in the vertical pod auto scaler and guy's going to bring it home and talk a little bit about the community and how you all can get involved and give us bug reports or pull requests or tell us our documentation stinks and we should make it better or we need more testing so i don't know how we doing on the on the tech situation here i guess okay [Music] [Applause] does anybody know any good jokes [Laughter] we just can't win for losing here you know all right well um [Music] so as many of you may or may not know uh for several releases now the horizontal pod auto scaler community has been working to release a v2 api and this work has been ongoing i think since before 1.22 it started off with v2 beta1 migrated to a v2 beta 2 status and just recently we've merged the pr to make the v2 stable and we've put out the deprecation notices for the previous versions and so if you're using v2 beta 1 and i imagine probably most people are not or if you're using v2 beta 2 you should be aware that you know we're coming up on 1.25 which will be the end of life for v2 beta1 v2 beta2 is also in deprecation right now but i think it will exist until 1.26 and then it will be deprecated as well now for the most part if you're using the horizontal pod auto scaler and you've been using the v2 beta 1 or v2 beta 2 apis you won't have to change much the serialization format ha
