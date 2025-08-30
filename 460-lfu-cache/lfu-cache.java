import java.util.*;

class LFUCache {
    private int capacity;
    private int minFrequency;
    private Map<Integer, Integer> keyToValue;
    private Map<Integer, Integer> keyToFrequency;
    private Map<Integer, LinkedHashSet<Integer>> frequencyToKeys;

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minFrequency = 1;
        this.keyToValue = new HashMap<>();
        this.keyToFrequency = new HashMap<>();
        this.frequencyToKeys = new HashMap<>();
    }

    public int get(int key) {
        if (!keyToValue.containsKey(key)) {
            return -1;
        }

        int frequency = keyToFrequency.get(key);
        keyToFrequency.put(key, frequency + 1);
        frequencyToKeys.get(frequency).remove(key);

        if (frequency == minFrequency && frequencyToKeys.get(frequency).isEmpty()) {
            minFrequency++;
        }

        frequencyToKeys.computeIfAbsent(frequency + 1, k -> new LinkedHashSet<>()).add(key);
        return keyToValue.get(key);
    }

    public void put(int key, int value) {
        if (capacity == 0) {
            return;
        }

        if (keyToValue.containsKey(key)) {
            keyToValue.put(key, value);
            get(key); // Increase frequency for the existing key
            return;
        }

        if (keyToValue.size() >= capacity) {
            int evictKey = frequencyToKeys.get(minFrequency).iterator().next();
            keyToValue.remove(evictKey);
            keyToFrequency.remove(evictKey);
            frequencyToKeys.get(minFrequency).remove(evictKey);
        }

        keyToValue.put(key, value);
        keyToFrequency.put(key, 1);
        frequencyToKeys.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
        minFrequency = 1;
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */