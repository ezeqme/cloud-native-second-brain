---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/zero-code-application-metrics-with-ebpf/
youtube_url: https://www.youtube.com/watch?v=AIDZ_owcd0o
youtube_search_url: https://www.youtube.com/results?search_query=Zero-code+application+metrics+with+eBPF+and+Prometheus+PromCon+2023
video_match_score: 1.023
status: video-found
---

# Zero-code application metrics with eBPF and Prometheus

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/zero-code-application-metrics-with-ebpf/
- YouTube: https://www.youtube.com/watch?v=AIDZ_owcd0o

## Resumo

Speaker(s): Nikola Grcevski & Mario Macias Instrumenting an existing application can require some toil, such as integrating instrumentation libraries, making changes to your code, as well as rebuilding and redeploying your packages. In order to soften your observability adoption, Grafana built the eBPF autoinstrument tool Beyla, which provides RED (Rate, Errors, Duration) metrics through Prometheus for your existing web services, whichever language they are written in. The eBPF tool is non-intrusive, i.e you don’t need to change any line of application code or configuration; you only need to deploy the auto-instrument tool in the same host as the service that you want to monitor.

## Abstract oficial

Speaker(s): Nikola Grcevski & Mario Macias

Instrumenting an existing application can require some toil, such as integrating instrumentation libraries, making changes to your code, as well as rebuilding and redeploying your packages. In order to soften your observability adoption, Grafana built the eBPF autoinstrument tool Beyla, which provides RED (Rate, Errors, Duration) metrics through Prometheus for your existing web services, whichever language they are written in.
The eBPF tool is non-intrusive, i.e you don’t need to change any line of application code or configuration; you only need to deploy the auto-instrument tool in the same host as the service that you want to monitor. Collecting monitoring data with the eBPF autoinstrument tool has very low overhead, and allows you to capture data about your runtime which is impossible with manual code instrumentation.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/zero-code-application-metrics-with-ebpf/
- YouTube: https://www.youtube.com/watch?v=AIDZ_owcd0o
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AIDZ_owcd0o
- YouTube title: PromCon 2023 - Zero-code application metrics with eBPF and Prometheus
- Match score: 1.023
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/zero-code-application-metrics-with-ebpf-and-prometheus/AIDZ_owcd0o.txt
- Transcript chars: 16999
- Keywords: metrics, instrument, kernel, application, traces, promethus, provide, export, languages, language, memory, process, ebpf, libraries, native, question, grafana, runtime

### Resumo baseado na transcript

[Music] thank you thank you very much thank you for the organization uh also uh my name is Mario Matias from grafana lab and today I will introduce you grafana Villa uh the the the product we are working on and how it can uh provide metrics from and traces from your application um using uh ebpf and Export them to promethus so imagine a a legacy application which is not instrumented and you just want to to get some some metrics from from it so in in the best

### Excerpt da transcript

[Music] thank you thank you very much thank you for the organization uh also uh my name is Mario Matias from grafana lab and today I will introduce you grafana Villa uh the the the product we are working on and how it can uh provide metrics from and traces from your application um using uh ebpf and Export them to promethus so imagine a a legacy application which is not instrumented and you just want to to get some some metrics from from it so in in the best case this is a very simplistic graph but uh if your application uses a a runtime like jbm or net you can insert an agent and with a bit of extra uh configuration you can push or pull your metrics from promethus but what happens with compiled languages like go rust C if you want to instrument it you need to get your code and add some instrumentation points then you rild it uh you get your instrument application and it's it's ready to work but uh with Legacy applications all code is not always uh is not always easy because you maybe don't have the time or the resources or for example the you are using a an old an old version of of the compiler or the run times and the you don't have Source level compatibility with with the newest latest versions of the the of the instrumentation libraries so baa uh comes here to fill this Gap and by means of evf is able to attach to some events of the E either the operating system or also you application as well as its runtime and and libraries and provide the the metrics for you without requiring to modify your your application you just need to deploy it with with with them evf it's a is a fancy word the first time I heard it is EVP what uh so let me first demystify a bit talking about what is not evf is not magic it's not something you can say Okay I I have a query language please evf show me all the information I want and format it to me so I I can purse it automatically is is is is not something uh like that uh what's more evf for me BPF looks like more a set of pip holes you have in in the in the kernel or you can set in your application and once you look into them you can see the Matrix there uh fortunately if you know where are you looking into you know how the data how the binary data is is structured and organized and then you can extract it so ebpf extended beray packet filter but some someone uh noticed me that it is not it was the original the the original name now it's evf doesn't have anything to do neither with Berkeley or packet filters uh it's a just in t
