from django.http import HttpResponse
from django.core.cache import caches
import time

def non_cached(request):
    # Эта функция не использует кэширование
    response_text = "This is a non-cached response. Current time: {}".format(time.time())
    return HttpResponse(response_text)

def localmemory_cached(request):
    cache = caches["default"]
    data = cache.get("localmemory_cached_data")

    if not data:
        time.sleep(2)  # Симулируем долгую операцию
        data = "Fresh content generated at: {}".format(time.time())
        cache.set("localmemory_cached_data", data, timeout=60)  # Кэшируем на 60 секунд

    response_text = "LocalMemory Cached Response: {} (Cached at: {})".format(
        data, time.time()
    )
    return HttpResponse(response_text)

def filesystem_cached(request):
    cache = caches["filesystem"]
    data = cache.get("filesystem_cached_data")

    if not data:
        time.sleep(2)  # Симулируем долгую операцию
        data = "Fresh content generated at: {}".format(time.time())
        cache.set("filesystem_cached_data", data, timeout=120)  # Кэшируем на 120 секунд

    response_text = "Filesystem Cached Response: {} (Cached at: {})".format(
        data, time.time()
    )
    return HttpResponse(response_text)

def database_cached(request):
    cache = caches["database"]
    data = cache.get("database_cached_data")

    if not data:
        time.sleep(2)  # Симулируем долгую операцию
        data = "Fresh content generated at: {}".format(time.time())
        cache.set("database_cached_data", data, timeout=300)  # Кэшируем на 300 секунд

    response_text = "Database Cached Response: {} (Cached at: {})".format(
        data, time.time()
    )
    return HttpResponse(response_text)

def dummy_cached(request):
    cache = caches["dummy"]
    data = cache.get("dummy_cached_data")

    if not data:
        time.sleep(2)  # Симулируем долгую операцию
        data = "Fresh content generated at: {}".format(time.time())
        cache.set("dummy_cached_data", data, timeout=60)  # Кэширование не работает

    response_text = "Dummy Cache Response (No Real Caching): {} (Generated at: {})".format(
        data, time.time()
    )
    return HttpResponse(response_text)