---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Experience"
themes: ["Cloud Native Experience"]
speakers: ["Wei Huang", "Apple", "Shiming Zhang", "DaoCloud"]
sched_url: https://kccnceu2025.sched.com/event/1txHR/a-comparative-analysis-of-kueue-volcano-and-yunikorn-wei-huang-apple-shiming-zhang-daocloud
youtube_search_url: https://www.youtube.com/results?search_query=A+Comparative+Analysis+of+Kueue%2C+Volcano%2C+and+YuniKorn+CNCF+KubeCon+2025
slides: []
status: parsed
---

# A Comparative Analysis of Kueue, Volcano, and YuniKorn - Wei Huang, Apple & Shiming Zhang, DaoCloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Cloud Native Experience]]
- País/cidade: United Kingdom / London
- Speakers: Wei Huang, Apple, Shiming Zhang, DaoCloud
- Schedule: https://kccnceu2025.sched.com/event/1txHR/a-comparative-analysis-of-kueue-volcano-and-yunikorn-wei-huang-apple-shiming-zhang-daocloud
- Busca YouTube: https://www.youtube.com/results?search_query=A+Comparative+Analysis+of+Kueue%2C+Volcano%2C+and+YuniKorn+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre A Comparative Analysis of Kueue, Volcano, and YuniKorn.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHR/a-comparative-analysis-of-kueue-volcano-and-yunikorn-wei-huang-apple-shiming-zhang-daocloud
- YouTube search: https://www.youtube.com/results?search_query=A+Comparative+Analysis+of+Kueue%2C+Volcano%2C+and+YuniKorn+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=njT5r3JjIaA
- YouTube title: A Comparative Analysis of Kueue, Volcano, and YuniKorn - Wei Huang, Apple & Shiming Zhang, DaoCloud
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/a-comparative-analysis-of-kueue-volcano-and-yunikorn/njT5r3JjIaA.txt
- Transcript chars: 21734
- Keywords: volcano, scheduling, scheduleuler, default, schedule, unicorn, basically, design, scheduled, number, testing, create, workloads, framework, controller, thanks, features, difference

### Resumo baseado na transcript

Thanks everyone to CubeCon and thanks thanks everyone for joining today's session. Uh today we are going to give you a comprehensive analysis on the popular schedulers in the market which are KQ, Volcano and the Unicorn which are most asked question among the uh audience we interact with. One things for a long time cube set is design originally designed for service service workloads. The second piece is that the native Kubernetes doesn't offer a good notion to maximize your clusters capacities. So uh but in terms of some advanced feature that is batch workloads needs it's better to design them in a multiq uh design so that some features can be more design implemented in a more natural way. It was original design its initial intent is put it as a side project so that it can involve the batch related capability uh at at its own pace and the finally merge with scriptul but due to some reasons it didn't go as planned

### Excerpt da transcript

Thanks everyone to CubeCon and thanks thanks everyone for joining today's session. Uh today we are going to give you a comprehensive analysis on the popular schedulers in the market which are KQ, Volcano and the Unicorn which are most asked question among the uh audience we interact with. Uh before that let's introduce ourselves. Uh my name is Wayan. I'm the co-chair and the maintainer of six scheduling and I work for Apple AML. H hello, my name is Shiming Jang work for dog in Shanghai and uh I'm the signal reviewer and the uh scheduling sub project co maintainer. All right. Uh today we are going to to firstly give you high level overview on the scheduulers what's their history and the relation with Kubernetes default scheduleuler and next going a deep dive on the features to help you better choose which may best fits your workloads and lastly give you some guidance and best practice on benchmark some particular feature of the scheduleuler. So firstly I think the question may be asked is that why there are so many scheduulers or what's missing in the cubeuler to serve like batch workloads.

So in my eyes there are three pieces that's maybe missing in the default scheduleuler as well as the native kubernetes. One things for a long time cube set is design originally designed for service service workloads. That means each pod is treated as an individual unit to do the scheduling cycle. that has a good size which is can be consistent to accommodate a part whole life cycle and to be have the uh unified integration with other components and all the APIs are imposed in the pod level but the downside is that we didn't give the job level scheduling constraint more attention which cause some decision that make for single part may not be nec necessarily optimal for a whole job for example GA scheduling. The second piece is that the native Kubernetes doesn't offer a good notion to maximize your clusters capacities. It only provides a static notion called resource coder and that is associated with the name space. But in the modernized organization they may want uh like a sharable coder and uh maybe even has hierarchical uh in that to to manage those kind of coder.

The third thing is the internal impation of the scheduleuler is a one setup just like the Excel London the hallways one que. So uh but in terms of some advanced feature that is batch workloads needs it's better to design them in a multiq uh design so that some features can be more design implemented in a mor
