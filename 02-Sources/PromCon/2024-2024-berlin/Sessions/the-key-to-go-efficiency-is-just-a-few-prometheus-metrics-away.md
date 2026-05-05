---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Cost Optimization"]
speakers: ["Arianna Vespri"]
source_url: https://promcon.io/2024-berlin/talks/the-key-to-go-efficiency-is-just-a-few-prometheus-metrics-away/
youtube_url: https://www.youtube.com/watch?v=7BaG2yT8B9Q
youtube_search_url: https://www.youtube.com/results?search_query=The+Key+to+Go+Efficiency+is+Just+a+Few+Prometheus+Metrics+Away%21+PromCon+2024
video_match_score: 1.035
status: video-found
---

# The Key to Go Efficiency is Just a Few Prometheus Metrics Away!

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: Arianna Vespri
- Página oficial: https://promcon.io/2024-berlin/talks/the-key-to-go-efficiency-is-just-a-few-prometheus-metrics-away/
- YouTube: https://www.youtube.com/watch?v=7BaG2yT8B9Q

## Resumo

Go Runtime is a key component that manages goroutines, memory allocations and garbage collection. It also tracks useful information about performance and state of your Go application, including Prometheus server itself. Do you know how to collect and use them on the scale?

## Abstract oficial

Go Runtime is a key component that manages goroutines, memory allocations and garbage collection. It also tracks useful information about performance and state of your Go application, including Prometheus server itself. Do you know how to collect and use them on the scale? Do you know why Prometheus added the reloadable “runtime.gogc” configuration in a recent version? Have you heard about a completely new runtime/metrics package released in Go 1.16?
In this talk, Arianna (Go developer and Prometheus clientgolang contributor) will bring you up to speed on using Prometheus metrics from Go Runtime! The audience will learn the importance and best practices of collecting Go Runtime metrics with Prometheus clientgolang, especially with the new Go runtime/metrics package. However, emphasis will be made on gaining actionable insights from specific metrics, discussing the bottlenecks it can detect and common optimizations to solve those!
Join us to learn how to leverage Go Runtime metrics to build faster, more reliable Go applications and use Prometheus server more efficiently on the way!

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/the-key-to-go-efficiency-is-just-a-few-prometheus-metrics-away/
- YouTube: https://www.youtube.com/watch?v=7BaG2yT8B9Q
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7BaG2yT8B9Q
- YouTube title: PromCon 2024 - The Key To Go Efficiency Is Just a Few Prometheus Metrics Away!
- Match score: 1.035
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/the-key-to-go-efficiency-is-just-a-few-prometheus-metrics-away/7BaG2yT8B9Q.txt
- Transcript chars: 27151
- Keywords: memory, metrics, application, matrix, metric, prometheus, runtime, actually, default, useful, especially, monitoring, understand, resources, already, client, metrix, garbage

### Resumo baseado na transcript

[Music] oh thank you so much very warm welcome so welcome everyone uh so it's my first time here and it's uh such a pleasure to be in front of you to talk about the importance of collecting Gan time metrics with Prometheus and also for Prometheus because as uh Matia said it's written in go right and this holds uh especially for development and not only for uh someone else you know running your applications uh in production so before I begin full disclosure so this presentation was originally

### Excerpt da transcript

[Music] oh thank you so much very warm welcome so welcome everyone uh so it's my first time here and it's uh such a pleasure to be in front of you to talk about the importance of collecting Gan time metrics with Prometheus and also for Prometheus because as uh Matia said it's written in go right and this holds uh especially for development and not only for uh someone else you know running your applications uh in production so before I begin full disclosure so this presentation was originally put together in a different version for goer cor UK this year 2024 by me and bner PKA who had all here yesterday was here helping setting me up I'm sure most of you know know him and this is why uh his GI up handle is here too and the slides are based on a similar template so it's like kind of the copyrighted bartex light style however uh here I'm proposing that talk in a little more prometheous users tailored manner so um during the time at my disposal I'll be talking about why monitoring go around time is fundamental and also for developers and uh then I'll go over ways uh of enabling those metrics with Prometheus and finally I will walk you through a few recommended metrics to understand them well but before all of these let me start with the number one uh existentialist question who am I my my name is AR V I've been a go developer for the last six years I'm a pritus cent Goan contributor for a year or so whereas my background is in the music industry when I'm not busy coding I dedicate myself to my passions which are synthesizers Gard in in history of art look at that beautiful baby there no be now before dealing with the first item on the agenda why monitoring G on time let's quickly remind ourselves about what go run time is so let's imagine you are running your go application so wherever it might be uh like Linux Mac Windows Windows uh it will run uh as an operating system process in that process instructions with the code you wrote which is whatever you put into your main function will be executed um which main function then likely spins up you know uh your go routines and will then execute some code um concurrently Etc um the operating system gives access to virtual memory which is uh theore space where you can allocate some physical memory for your application like uh data for Global variables code instructions stock for objects with a lifetime scope to your functions and Heap um which typically is the biggest for objects with more of a dynamic kind of Lifeti
