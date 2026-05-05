---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Akilan Selvacoumar", "Florent Poinsard", "Planetscale"]
sched_url: https://kccnceu2021.sched.com/event/iaAj/graduated-project-lightning-talk-vitess-are-we-fast-yet-akilan-selvacoumar-florent-poinsard-planetscale
youtube_search_url: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Vitess%2C+are+we+Fast+Yet%3F+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Graduated Project Lightning Talk: Vitess, are we Fast Yet? - Akilan Selvacoumar, Florent Poinsard, Planetscale

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Akilan Selvacoumar, Florent Poinsard, Planetscale
- Schedule: https://kccnceu2021.sched.com/event/iaAj/graduated-project-lightning-talk-vitess-are-we-fast-yet-akilan-selvacoumar-florent-poinsard-planetscale
- Busca YouTube: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Vitess%2C+are+we+Fast+Yet%3F+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Graduated Project Lightning Talk: Vitess, are we Fast Yet?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iaAj/graduated-project-lightning-talk-vitess-are-we-fast-yet-akilan-selvacoumar-florent-poinsard-planetscale
- YouTube search: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Vitess%2C+are+we+Fast+Yet%3F+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=h1bd1yxA4ec
- YouTube title: Graduated Project Lightning Talk: Vitess, are we Fast Yet? - Akilan Selvacoumar, Florent Poinsard
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/graduated-project-lightning-talk-vitess-are-we-fast-yet/h1bd1yxA4ec.txt
- Transcript chars: 6871
- Keywords: benchmark, benchmarks, execute, results, configuration, github, reliable, database, everything, hardware, widely, benchmarking, automated, commits, server, dashboards, metrics, mentioned

### Resumo baseado na transcript

so today's talk is on betas rv fast shape by mia keelan and florent um a bit of a background with this with this is a database solution for deploying scaling and managing large clusters of open source database instances with this is based on mysql slash more adb it's massively scalable it is a cncf graduated project with this runs both on public and private infrastructure and works very well with dedicated hardware bethes has over 24 000 comments it's being used widely by companies like youtube slack jd.com

### Excerpt da transcript

so today's talk is on betas rv fast shape by mia keelan and florent um a bit of a background with this with this is a database solution for deploying scaling and managing large clusters of open source database instances with this is based on mysql slash more adb it's massively scalable it is a cncf graduated project with this runs both on public and private infrastructure and works very well with dedicated hardware bethes has over 24 000 comments it's being used widely by companies like youtube slack jd.com github and pinterest and is pretty popular among the dbas for horizontally scaling mysql databases i'd like to give it over to florent talk more about today's talk great thank you yes um just like you said uh it is being widely used more and more in bigger and bigger systems but this comes down to two problems um we have to ensure that vita cisco base is reliable um and also it has a good performance this is too big attribute that we want so how do we ensure reliability well we have test unit test end-to-end test um everything goes through cisd pipelines and et cetera but how about performances well we have benchmarks and today we're going to cover how to benchmark a big project just like venus we come up with five pilots on how to benchmark a new principles project such as vitesse first we want it to be easy uh we want to foster a culture of benchmarking we want to encourage people to do more and more benchmarks secondly we also want it to be automated just like unit test we want to avoid human error we want to spend more time on important things and so on then we also want it to be reliable uh you know benchmarks result is not a boolean uh it's not like unit test pass or failed uh everything is measured in nanoseconds so it has to be reliable then we also want it to be reproducible we want to resolve i mean we want to allow engineers to debug a benchmark if there's an issue or a spike in performance we also want it to be observable um you know we want to see results we want to see reports we want them to be accessible by anyone in the community so how did we achieve that well we've created are we fast yet it is an automated benchmarking monitoring tool for vtest uh it is open sourced of course and version number two is being developed in golden at the moment um we execute different types of benchmark in our fast yet we have macro benchmarks and micro benchmarks the first one uh we have otp and tpcc which are two different types of micro benchmarks tha
